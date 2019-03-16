"""
    功能点1：AQI计算
    知识点1：
    功能点2：AQI计算，JSON读写
    知识点2:
        json.dumps, json.load, json.dump
        list.sort(func) func可以用lambda函数实现
    功能点3：AQI计算，csv写
    知识点3:
        writer = csv.writer(f)
        writer.writerow(line)
    功能点4：AQI计算，csv读
    知识点4:
        使用with语句操作文件对象
            with open(file) as somefile:
                for line in somefile:
                    print(line)
        csv.reader()
        os模块 系统/目录相关功能，不受平台限制
            os.path.splitext()
        字符串.join(list)
"""
import json
import csv
import os


def process_csv_file(filepath):
    """
        解码csv文件
    """
    with open(filepath, mode='r', encoding='UTF-8', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(', '.join(row))


def process_json_file(filepath):
    """
        解码json文件
    """
    with open(filepath, mode='r', encoding='UTF-8') as f:
        city_list = json.load(f)
    print(city_list)


def main():
    """
        主函数
    """
    filepath = input('请输入文件名称：')
    filename, file_ext = os.path.splitext(filepath)

    if file_ext.lower() == '.json':
        # json文件
        process_json_file(filepath)
    elif file_ext.lower() == '.csv':
        # csv文件
        process_csv_file(filepath)
    else:
        print('不支持的文件格式')


if __name__ == '__main__':
    main()
