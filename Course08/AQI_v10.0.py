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
    功能点7：AQI计算，数据分析
    知识点7:Pandas模块
        Series 一维数组
            ser_obj = pd.Series(range(10))
            ser_obj.index ser_obj.values
        DataFrame 多维数组
        数据过滤
"""
import pandas as pd
import matplotlib.pyplot as plt

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def main():
    """
        主函数
    """
    aqi_data = pd.read_csv('china_city_aqi.csv')
    print('基本信息：')
    print(aqi_data.info())

    print('数据预览：')
    print(aqi_data.head())

    # 数据清洗
    # 只保留AQI大于0的数据
    # filter_cond = aqi_data['AQI'] > 0
    # clean_aqi_data = aqi_data[filter_cond]

    clean_aqi_data = aqi_data[aqi_data['AQI'] > 0]

    # 基本统计
    print('AQI最大值：', aqi_data['AQI'].max())
    print('AQI最小值：', aqi_data['AQI'].min())
    print('AQI最小值(Clean)：', clean_aqi_data['AQI'].min())
    print('AQI均值：', aqi_data['AQI'].mean())
    print('AQI均值(Clean)：', clean_aqi_data['AQI'].mean())

    # 按AQI排序,Top50
    top50_cities = clean_aqi_data.sort_values(by=['AQI'], ascending=True).head(50)
    top50_cities.plot(kind='bar', x='city', y='AQI', title='空气质量Best50', figsize=(20, 10))
    plt.savefig('top50_aqi_bar.png')
    plt.show()


if __name__ == '__main__':
    main()
