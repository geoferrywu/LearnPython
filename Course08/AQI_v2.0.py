"""
    功能点1：AQI计算
    知识点1：
    功能点1：AQI计算，JSON读取
    知识点2:
        json.dumps, json.load, json.dump
        list.sort(func) func可以用lambda函数实现
"""
import json


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

    f = open('top5.json', mode='w', encoding='UTF-8')
    json.dump(top5_list, f, ensure_ascii=False)
    f.close()


if __name__ == '__main__':
    main()
