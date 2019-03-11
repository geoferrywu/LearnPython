"""
    功能1：密码强度判断
    知识点1：str.isnumeric() str.isalpha() str.islower() str.isupper() isxxx..()

    功能2：输错次数限制，中止循环
    知识点2:continue bread
"""


def check_number_exist(password_str):
    """
            判断子字符串中是否有数字
    """
    has_number = False
    for c in password_str:
        if c.isnumeric():
            has_number = True
            break
    return has_number


def check_letter_exist(password_str):
    """
            判断子字符串中是否有字母
    """
    has_letter = False
    for c in password_str:
        if c.isalpha():
            has_letter = True
            break
    return has_letter


def main():
    """
        主函数
    """
    try_times = 5
    times = 1

    while times <= try_times:
        password = input('请输入密码(第{}次)：'.format(times))
        times += 1

        # 密码强度
        strength_level = 0

        # 规则1 密码长度大于8
        if len(password) >= 8:
            strength_level += 1
        else:
            print('密码长度要求至少8位')

        # 规则2 要有数字
        if check_number_exist(password):
            strength_level += 1
        else:
            print('密码要求包含数字')
            continue

        # 规则3 要有字母
        if check_letter_exist(password):
            strength_level += 1
        else:
            print('密码要求包含字母')
            continue

        if strength_level == 3:
            print('密码强度合格')
            break
        else:
            print('密码强度不合格')

    if times > try_times:
        print('错误次数过多！')


if __name__ == '__main__':
    main()
