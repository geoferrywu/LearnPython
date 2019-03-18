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
    功能点7：AQI计算，数据分析，网络爬虫，beautifulsoup4
    知识点7:
        Pandas模块
        Series 一维数组
            ser_obj = pd.Series(range(10))
            ser_obj.index ser_obj.values
        DataFrame 多维数组
"""
import pandas as pd


def main():
    """
        主函数
    """
    aqi_data = pd.read_csv('china_city_aqi.csv')
    print('基本信息：', type(aqi_data))
    print(aqi_data.info())

    print('数据预览：')
    print(aqi_data.head())

    # 基本统计
    print('AQI最大值：', aqi_data['AQI'].max())
    print('AQI最小值：', aqi_data['AQI'].min())
    print('AQI均值：', aqi_data['AQI'].mean())

    # 按AQI排序,Top10
    top10_cities = aqi_data.sort_values(by=['AQI'], ascending=True).head(10)
    print('空气质量最好的10个城市：')
    print(top10_cities)

    # 按AQI排序,bottom10
    # botom10_cities = aqi_data.sort_values(by=['AQI'], ascending=True).tail(10)
    botom10_cities = aqi_data.sort_values(by=['AQI'], ascending=False).head(10)
    print('空气质量最差的10个城市：')
    print(botom10_cities)

    # 保存csv文件
    top10_cities.to_csv('top10_aqi.csv', index=False)
    botom10_cities.to_csv('bottom10_aqi.csv', index=False)


if __name__ == '__main__':
    main()
