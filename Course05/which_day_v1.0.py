"""
    功能：输入年月日，计算第几天
    知识点：元组(tuple)
        tuple = (x, y, ...)
        元组中的值不能修改
        函数返回多个值可以用元组 return a, b, c...
"""
from datetime import datetime


def main():
    """
        主函数
    """
    day_in_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    date_str = input('请输入日期(yyyy/mm/dd)：')
    dt: datetime = datetime.strptime(date_str, '%Y/%m/%d')
    days = sum(day_in_month[0:dt.month - 1]) + dt.day

    if (dt.year % 400) == 0 or (dt.year % 4 == 0 and dt.year % 100 != 0):
        # 闰年
        if dt.month > 2:
            # 闰月后
            days += 1

    print(days)


if __name__ == '__main__':
    main()

