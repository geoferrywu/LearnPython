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
    # 初始化列表【0，0，0，0，0，0...】
    result_list = [0] * 11
    roll_list = list(range(2, 13))

    roll_dict = dict(zip(roll_list, result_list))

    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()
        roll_dict[roll1 + roll2] += 1

    for i, result in roll_dict.items():
        print('点数 {} 的次数 {}, 频率：{}'.format(i, result, result / total_times))

    # for key in roll_dict.items():
    #     print('点数 {} 的次数 {}, 频率：{}'.format(key[0], key[1], key[1] / total_times))

    # print(result_list)


if __name__ == '__main__':
    main()
