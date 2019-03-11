"""
    功能：输入年月日，计算第几天
    功能：列表替换元组
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
    # day_in_month_tuple = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    day_in_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    date_str = input('请输入日期(yyyy/mm/dd)：')
    dt: datetime = datetime.strptime(date_str, '%Y/%m/%d')

    if is_leap_year(dt.year):
        # 闰年
        day_in_month_list[1] = 29

    days = sum(day_in_month_list[0:dt.month - 1]) + dt.day

    print('这是{}年的{}天'.format(dt.year, days))


if __name__ == '__main__':
    main()

