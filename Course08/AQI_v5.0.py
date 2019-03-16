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
"""
import requests


def get_html_text(url):
    """
        返回URL文本
    """
    r = requests.get(url, timeout=30)
    # print(r.status_code)
    return r.text


def main():
    """
        主函数
    """
    city_pinyin = input('请输入城市拼音：')
    url = 'http://pm25.in/' + city_pinyin
    url_text = get_html_text(url)

    aqi_div = '''<div class="span12 data">
        <div class="span1">
          <div class="value">
            '''

    index = url_text.find(aqi_div)
    begin_index = index + len(aqi_div)
    end_index = begin_index + 2
    aqi_val = url_text[begin_index:end_index]
    print('空气质量为：{}'.format(aqi_val))


if __name__ == '__main__':
    main()
