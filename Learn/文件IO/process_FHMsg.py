import os
import glob # 文件名模式匹配库
import chardet
import csv
import pandas as pd
import re
import time
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            begin = time.time()
            r = func(*args, **kw)
            end = time.time()
            print('%s executed in %s ms' % (func.__name__, 1000 * (end - begin)))
            return r
        return wrapper
    return decorator

# 多语言一览
lang_list = ['jpn','chs','cht','eng','esp','fra','ita','deu','pol','vie','kor']
# 基准语言索引
base_lang_idx = 0  # 0=jpn,1=chs,...
# 文言文件目录
rootdir = 'D:/HYRON_input_AI_190308/FZ-Application/FZ_FH_FJ-XXX.610/Release_XP/Message/'

# 正则表达式匹配 AAA=BBBB字符串
patt= r'^((?![;]).+=.*)$'
p_multi=re.compile(patt, re.MULTILINE)

def detect_file_Code(path):
    '''
        取得文件编码, utf-8...
    '''
    with open(path, 'rb') as file:
        data = file.read(1000)
        dicts = chardet.detect(data)
    return dicts["encoding"]


def get_msgfile_list(lang):
    '''
        根据语言索引取得单一语言的文件一览
    '''
    filelist = glob.glob(rootdir + '*{}.msg'.format(lang))
    return filelist


def merge_dict(dict_m, dict_l):
    '''
        合并文言字典
    '''
    errcnt = 0
    dict_len = len(dict_l)

    for key, value in dict_m.items():
        
        if key == '[Ident]':
            continue
        
        if dict_len > 0:
            try:
                value.append(dict_l[key][-1])
            except KeyError:
                value.append('#error')
                errcnt += 1
        else:
            value.append('#file miss')

    return errcnt


def get_msg_dict(fn):
    '''
        读取文言文件，返回文件字典
    '''
    method = 1  # 1:使用传统方法 2:使用正则表达式分隔 3:使用函数式编程

    dict_file = {}
    file_enc = detect_file_Code(fn)
    with open(fn, "r", encoding=file_enc, newline='') as msg_file:
        if method == 1:   # 使用传统方法
            allLines = msg_file.readlines()

            for line in allLines:
                if '=' in line and line[0] != ';':
                    strsp = line[:-2].split('=', 1) # 要去掉最后的 \r\n
                    dict_file[strsp[0]] = [strsp[0],strsp[1]]
        elif method == 2:   # 使用正则表达式匹配
            allTxt = msg_file.read()
            
            result = p_multi.findall(allTxt)  # 正则表达式匹配 AAA=BBBB字符串
            for rep in result:
                strsp = rep[:-1].split('=', 1)      # 要去掉最后的 \r
                dict_file[strsp[0]] = [strsp[0],strsp[1]]
        elif method == 3:    # 使用函数式编程
            allLines = msg_file.readlines()
            flt = filter(lambda x:'=' in x and x[0] != ';', allLines)
            dict_file = dict(map(split_msg, flt))

    return dict_file

def split_msg(line):
    '''
        返回[a,b]形式的列表
        通过map()函数形成，[[a1,b1],[a2,b2],[a3,b3]...]
        然后转换成dict:{a1:b1,a2:b2,a3:b3,...}
    '''
    sp = line.split('=',1)
    return [sp[0],[sp[0],sp[1][:-2]]]   # 要去掉最后的 \r\n，返回 [a,b] 形式的列表

def make_csv_file(msglist, unit_name):
    '''
        文言字典文件保存到CSV文件
    '''
    dir = os.path.join(os.getcwd(), 'Result')
    if not os.path.isdir(dir):
        os.mkdir(dir)
    fn = os.path.join(dir,'{}.csv'.format(unit_name))

    '''
    # 使用DataFrame生成CSV
    df = pd.DataFrame(msglist)
    # UTF-8-sig是带BOM格式
    df.to_csv(fn, encoding='UTF-8-sig', header=False)
    '''

    # 自己写CSV
    with open(fn, 'w', encoding='UTF-8-sig', newline='') as fw:
        writer = csv.writer(fw)
        for msgLine in msglist:
            writer.writerow(msgLine)


def process_filelist(filelist):
    '''
        处理所有文言文件
    '''
    base_lang = lang_list[base_lang_idx]

    for name in filelist:
        errcnt = 0
        filemiss = 0

        key_ident = '[Ident]'
        dict_main = {key_ident: ['Ident'] + lang_list}
        
        # 生成基准文言字典
        dict_main.update(get_msg_dict(name))

        file_name = os.path.basename(name)
        file_dir = os.path.dirname(name)

        for _lang in lang_list:
            if _lang == base_lang:
                continue

            next_file = file_name.replace('_{}'.format(base_lang), '_{}'.format(_lang))
            next_path = os.path.join(file_dir, next_file)

            if os.path.isfile(next_path):
                dict_next = get_msg_dict(next_path)
                # 合并文言字典
                errcnt += merge_dict(dict_main, dict_next)
            else:
                filemiss += 1
                merge_dict(dict_main, {})

        make_csv_file(dict_main.values(), '_{}_{}_'.format(filemiss, errcnt) + file_name.split('_')[0])

    # print('发现{}个识别子错误'.format(errcnt), '缺少{}个语言文件'.format(filemiss))

@log('')
def main():
    """
        主函数
    """
    process_filelist(get_msgfile_list(lang_list[base_lang_idx]))


if __name__ == '__main__':
    main()