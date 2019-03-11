"""
    功能：52周阶梯式存钱
    功能：记录每周存款数
    功能：使用循环直接计数
        for <x> in <list>:
            <body>

        range(n) = [0, 1, ...,n-1]
    知识点：列表（可以合并+ ，可以重复 * n ，取长度 len(list)，判断包含元素 x in list，......）
    知识点：math
"""
import math


def main():
    """
        主函数
    """
    # 每周的存入金额
    money_per_week = 100
    # 递增金额
    increase = 200

    # 周数
    # week = 1

    # 总周数
    total_weeks = 52

    # 账户累计
    saving = 0

    # 记录每周存款数列表
    money_list = []

    for week in range(total_weeks):
        # week是从 0 ~ total_weeks - 1
        # 存钱操作
        money_list.append(money_per_week)
        saving = math.fsum(money_list)

        # 更新下周存钱金额
        money_per_week += increase

        # 输出信息
        print('第{}周，存入{}元，账户累计{}元'.format(week + 1, money_list[week], saving))


if __name__ == '__main__':
    main()
