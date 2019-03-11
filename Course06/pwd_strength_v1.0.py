"""
    功能1：密码强度判断
    知识点1：str.isnumeric() str.isalpha() str.islower() str.isupper() isxxx..()
"""


def check_number_exist(password_str):
    """
            判断子字符串中是否有数字
    """
    judge = False
    for c in password_str:
        if c.isnumeric():
            judge = True
            break
    return judge


def check_letter_exist(password_str):
    """
            判断子字符串中是否有字母
    """
    judge = False
    for c in password_str:
        if c.isalpha():
            judge = True
            break
    return judge


def main():
    """
        主函数
    """
    password = input('请输入密码：')

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

    # 规则3 要有字母
    if check_letter_exist(password):
        strength_level += 1
    else:
        print('密码要求包含字母')

    if strength_level == 3:
        print('密码强度合格')
    else:
        print('密码强度不合格')


if __name__ == '__main__':
    main()
