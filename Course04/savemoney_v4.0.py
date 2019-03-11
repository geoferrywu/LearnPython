"""
    功能：52周阶梯式存钱
    功能：记录每周存款数
    功能：使用循环直接计数
        for <x> in <list>:
            <body>
        range(n) = [0, 1, ...,n-1]
    功能：参数手工输入
    知识点：列表（可以合并+ ，可以重复 * n ，取长度 len(list)，判断包含元素 x in list，......）
    知识点：math
    知识点：函数返回值，变量作用域
"""
import math

# 全局变量
# 账户累计
saving_all = 0


def save_money_in_n_week(money_per_week, increase, total_weeks):
    # 申明全局变量
    global saving_all

    # 记录每周存款数列表
    money_list = []

    for week in range(total_weeks):
        # week是从 0 ~ total_weeks - 1
        # 存钱操作
        money_list.append(money_per_week)
        saving_all = math.fsum(money_list)

        # 更新下周存钱金额
        money_per_week += increase

        # 输出信息
        print('第{}周，存入{}元，账户累计{}元'.format(
            week + 1, money_list[week], saving_all))

    return saving_all


def main():
    """
        主函数
    """
    # 每周的存入金额
    # money_per_week = 100
    money_per_week = float(input('请输入每周存入金额：'))

    # 递增金额
    # increase = 200
    increase = float(input('请输入每周递增金额：'))

    # 总周数
    # total_weeks = 52
    total_weeks = int(input('请输入存钱周数：'))

    # 账户累计(全局)
    global saving_all

    # 账户累计(内部)
    saving_in = 0

    # 调用函数
    saving_in = save_money_in_n_week(money_per_week, increase, total_weeks)
    print('总金额是{}元 (从函数返回)'.format(saving_in))
    print('总金额是{}元 (从全局变量)'.format(saving_all))


if __name__ == '__main__':
    main()
