"""
    功能：输入年月日，计算第几天
    功能：列表替换元组
    功能：使用集合 {x, y, ...}
    知识点：元组(tuple)
        tuple = (x, y, ...)
        元组中的值不能修改
        函数返回多个值可以用元组 return a, b, c...
"""
from datetime import datetime


def is_leap_year(year):
    """
        判断year是否为闰年
        是返回True， 否返回False
    """
    is_leap = False
    if (year % 400) == 0 or (year % 4 == 0 and year % 100 != 0):
        # 闰年
        is_leap = True

    return is_leap


def main():
    """
        主函数
    """
    date_str = input('请输入日期(yyyy/mm/dd)：')
    dt: datetime = datetime.strptime(date_str, '%Y/%m/%d')

    # 30天的集合
    _30_days_month_set = {4, 6, 9, 11}
    # 31天的集合
    _31_days_month_set = {1, 3, 5, 7, 8, 10, 12}

    # 初始值
    days = dt.day

    for i in range(1, dt.month):
        # range(1, dt.month): range的list从 1 开始
        if i in _30_days_month_set:
            days += 30
        elif i in _31_days_month_set:
            days += 31
        else:
            days += 28

    if is_leap_year(dt.year) and dt.month > 2:
        # 闰年
        days += 1

    print('这是{}年的{}天'.format(dt.year, days))


if __name__ == '__main__':
    main()
