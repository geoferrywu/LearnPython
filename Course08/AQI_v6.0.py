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
    功能点5：AQI计算，网络爬虫
    知识点5:
        requests模块
        get() post()
        status_code HTTP请求的返回状态
    功能点6：AQI计算，网络爬虫，beautifulsoup4
    知识点5:
        requests模块
        get() post()
        status_code HTTP请求的返回状态
"""
import requests
from bs4 import BeautifulSoup


def get_city_aqi(city_pinyin):
    """
        获取城市的AQI
    """
    url = 'http://pm25.in/' + city_pinyin
    r = requests.get(url, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')
    div_list = soup.find_all('div', {'class': 'span1'})

    city_aqi = []
    for i in range(8):
        div_content = div_list[i]
        cation = div_content.find('div', {'class': 'caption'}).text.strip()
        value = div_content.find('div', {'class': 'value'}).text.strip()

        city_aqi.append((cation, value))

    return city_aqi


def main():
    """
        主函数
    """
    city_pinyin = input('请输入城市拼音：')
    city_aqi = get_city_aqi(city_pinyin)
    print(city_aqi)


if __name__ == '__main__':
    main()
