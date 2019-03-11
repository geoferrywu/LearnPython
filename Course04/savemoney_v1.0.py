"""
    功能：52周阶梯式存钱
    知识点：
"""


def main():
    """
        主函数
    """
    # 每周的存入金额
    money_per_week = 100
    # 递增金额
    increase = 200
    # 周数
    week = 1
    # 总周数
    total_weeks = 52

    # 账户累计
    saving = 0

    while week <= total_weeks:
        # 存钱操作
        saving += money_per_week

        # 输出信息
        print('第{}周，存入{}元，账户累计{}元'.format(week, money_per_week, saving))

        # 更新下周存钱金额
        money_per_week += increase
        week += 1


if __name__ == '__main__':
    main()
