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
"""
import random
import matplotlib.pyplot as plt

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def roll_dice():
    """
        模拟掷骰子
    """
    roll = random.randint(1, 6)
    return roll


def main():
    """
        主函数
    """
    total_times = 10000

    #  记录骰子1的结果
    roll_list = []

    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()
        roll_list.append(roll1 + roll2)

    # 数据分析
    plt.hist(roll_list, list(range(2, 14)), density=1, edgecolor='black', linewidth=1)
    plt.title('骰子点数统计')
    plt.xlabel('点数')
    plt.ylabel('频率')

    plt.show()


if __name__ == '__main__':
    main()
