"""
    功能点1：随机数
    知识点1：
        random模块
        enumerate() 函数 将可遍历的组合转换为索引序列
"""
import random


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
    total_times = 1000
    # 初始化列表【0，0，0，0，0，0】
    result_list = [0] * 6

    for i in range(total_times):
        roll = roll_dice()
        result_list[roll - 1] += 1

    for i, result in enumerate(result_list):
        print('点数 {} 的次数 {}, 频率：{}'.format(i + 1, result, result / total_times))

    # print(result_list)


if __name__ == '__main__':
    main()
