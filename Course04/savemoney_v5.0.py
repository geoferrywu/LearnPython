"""
    功能：52周阶梯式存钱
    功能：记录每周存款数
    功能：使用循环直接计数
        for <x> in <list>:
            <body>
        range(n) = [0, 1, ...,n-1]
    功能：参数手工输入
    功能：输入日期，得到存款数
    知识点：列表（可以合并+ ，可以重复 * n ，取长度 len(list)，判断包含元素 x in list，......）
    知识点：math
    知识点：函数返回值，变量作用域
    知识点：处理时间（时间日期库） import datetime
        datetime.datetime.strptime(date_str, '%Y/%m/%d') 解析日期字符串（字符串->日期）
        datetime.datetime.strftime(datetime, '%Y/%m/%d') 格式化日期（日期->字符串）
"""
import math
import datetime

# 全局变量
# 账户累计
saving_all = 0


def save_money_in_n_week(money_per_week, increase, total_weeks):
    # 申明全局变量
    global saving_all

    # 记录每周存款数列表
    money_list = []
    # 记录每周存款数累计
    save_list = []

    for week in range(total_weeks):
        # week是从 0 ~ total_weeks - 1
        # 存钱操作
        money_list.append(money_per_week)
        saving_all = math.fsum(money_list)
        save_list.append(saving_all)

        # 更新下周存钱金额
        money_per_week += increase

        # 输出信息
        # print('第{}周，存入{}元，账户累计{}元'.format(
        #     week + 1, money_list[week], saving_all))

    return save_list


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

    # 调用函数
    saving_list = save_money_in_n_week(money_per_week, increase, total_weeks)

    date_str = input('请输入日期(yyyy/mm/dd)：')
    dt: datetime = datetime.datetime.strptime(date_str, '%Y/%m/%d')
    week_num = dt.isocalendar()[1]   # (年， 周， 日) 中取周数

    # week_num = int(input('请输入第几周：'))
    print('第{}周存款金额是{}元。'.format(week_num, saving_list[week_num - 1]))


if __name__ == '__main__':
    main()
