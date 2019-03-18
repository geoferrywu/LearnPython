
from functools import reduce

def multi(a,b):
    return a*b

def test():
    # 生成一个列表（可迭代对象）
    list_a = list(range(1,10))
    rest = reduce(multi,list_a)
    print(rest)


def main():
    """
        主函数
    """
    test()

if __name__ == '__main__':
    main()
