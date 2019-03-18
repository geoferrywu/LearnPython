"""
    
"""


def test():
    # (名字，分数)的列表
    list_b = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

    # 按名字排序
    rest = sorted(list_b, key=lambda x: x[0])
    print(rest)
    # 按分数排序
    rest = sorted(list_b, key=lambda x: x[1])
    print(rest)

def main():
    """
        主函数
    """
    test()

if __name__ == '__main__':
    main()
