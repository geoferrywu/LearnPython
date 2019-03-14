"""
    功能点1：随机数
    知识点1：
        random模块
        enumerate() 函数 将可遍历的组合转换为索引序列
    功能点2：模拟2个骰子
    知识点：
        zip() 函数 将对应的元素打包成元组
            zip(list1, list2) list1 和 list2 的元素个数相同
            dict(zip(list1, list2)) 构建字典
    功能点3：投掷结果数据可视化
    知识点：
        matplotlib库
        import matplotlib.pyplot as plt
        plt.scatter(x, y)
        plt.show()
    功能点4：投掷结果数据分析
    知识点：
        直方图
        plt.hist()
    功能点5：使用科学计算库简化程序
    知识点：
        numpy
        np.random.randint(a,b,size)  [a,b]间形状为size的数组
        plt.hist()
"""
import random
import matplotlib.pyplot as plt
import numpy as np

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def main():
    """
        主函数
    """
    total_times = 10000

    #  记录骰子1的结果
    roll1_arr = np.random.randint(1, 7, size=total_times)
    roll2_arr = np.random.randint(1, 7, size=total_times)
    result_arr = roll1_arr + roll2_arr

    hist, bins = np.histogram(result_arr, bins=range(2, 14))
    print(hist)
    print(bins)

    # 数据分析
    plt.hist(result_arr, bins=range(2, 14), density=1, edgecolor='black', linewidth=1, rwidth=0.8)

    # 设置坐标点显示
    tick_label = ['2点', '3点', '4点', '5点', '6点','7点', '8点', '9点', '10点', '11点', '12点']
    tick_pos = np.arange(2, 13) + 0.5
    plt.xticks(tick_pos, tick_label)

    plt.title('骰子点数统计')
    plt.xlabel('点数')
    plt.ylabel('频率')

    plt.show()


if __name__ == '__main__':
    main()
