"""
    功能：BMR 计算器
"""


def main():
    """
        主函数
    """
    y_or_n = input('是否退出程序(y/n)?')

    while y_or_n != 'y':

        # 性别
        gender = input('性别：')

        # 体重(KG)
        weight = input('体重(kg)：')

        # 身高(CM)
        height = input('身高(cm)：')

        # 年龄
        age = input('年龄：')

        if gender == '男':
            # 男性
            bmr = (13.7 * float(weight)) + (5.0 * float(height)) - (6.8 * int(age)) + 66
        elif gender == '女':
            # 女性
            bmr = (9.6 * float(weight)) + (1.8 * float(height)) - (4.7 * int(age)) + 655
        else:
            bmr = -1

        if bmr != -1:
            print('基础代谢率（大卡）：', bmr)
        else:
            print('不支持该性别')

        print()
        y_or_n = input('是否退出程序(y/n)?')


if __name__ == '__main__':
    main()
