"""
    功能点1：AQI计算
    知识点1：
    功能点2：AQI计算，JSON读写
    知识点2:
        json.dumps, json.load, json.dump
        list.sort(func) func可以用lambda函数实现
    功能点3：AQI计算，csv读写
    知识点3:
        writer = csv.writer(f)
        writer.writerow(line)
"""
import json
import csv


def process_json_file(filepath):
    """
        解码json文件
    """
    f = open(filepath, mode='r', encoding='UTF-8')
    city_list = json.load(f)
    f.close()
    return city_list


def main():
    """
        主函数
    """
    filepath = input('请输入json文件名称：')
    city_list = process_json_file(filepath)

    # 打出来看一下
    print(city_list)

    # city只是一个名字，代表list中的一项（此处list的项为字典）
    city_list.sort(key=lambda city: city['aqi'], reverse=True )
    # 再打出来看一下
    print(city_list)

    top5_list = city_list[:5]

    lines = list()
    # 表头
    lines.append(list(top5_list[0].keys()))

    for city in top5_list:
        lines.append(list(city.values()))

    f = open('top5.csv', mode='w', encoding='UTF-8', newline='')
    writer = csv.writer(f)
    for line in lines:
        writer.writerow(line)
    f.close()


if __name__ == '__main__':
    main()
