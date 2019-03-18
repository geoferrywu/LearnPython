
import os

curdir = os.path.dirname(__file__)

def test_file_open():
    # 打开一个文件
    fo = open(curdir + "\\foo.txt", "w")
    print("文件名: ", fo.name)
    print("是否已关闭 : ", fo.closed)
    print("访问模式 : ", fo.mode)
    string = 'hello World\n'
    fo.write(string)
    fo.write('''sfsdf
sfsfsdf
sdfsdf''')
    fo.close()


def test_file_read():
    # read file by per line 
    fo = open(curdir + '\\china_city_aqi.csv', "r", encoding='utf-8', newline='')
    while True:
        linetxt = fo.readline() # 读取到的行末是包含换行的
        if not linetxt:
            break
        print(linetxt[:-2]) # 读取到的行末是包含换行的\r\n (根据打开方式 newline)
        # print(linetxt[:].encode('utf-8')) # 读取到的行末是包含换行的（通过字节数组验证）
    fo.close()

    # # read file allline 
    # with open(curdir + '\\china_city_aqi.csv', "r", encoding='utf-8', newline='') as f:
    #     allLines = f.readlines()
    #     for line in allLines:
    #         print(line[:-2])    # 读取到的行末是包含换行的\r\n (根据打开方式 newline)


    # with open(curdir + '\\china_city_aqi.csv', "r", encoding='utf-8', newline='') as f:
    #     allLines = f.readlines()
    #     print(len(allLines))
    #     for i in range(len(allLines)):
    #         print(allLines[i][:-2]) # 读取到的行末是包含换行的\r\n (根据打开方式 newline)

import chardet
def test_file_detectCode():
    path = curdir + '\\china_city_aqi.csv'
    with open(path, 'rb') as file:
        data = file.read(1000)
        dicts = chardet.detect(data)
    print(dicts["encoding"])
    # return 


def main():
    """
        主函数
    """
    # test_file_open()
    # test_file_read()
    test_file_detectCode()

if __name__ == '__main__':
    main()


