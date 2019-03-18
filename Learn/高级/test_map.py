'''
    f(x) = x + 1
'''
def func(x):
    # func 是传入的函数参数
    return x ** 2

def lambda_func(x):
    '''
        返回一个lambda表达式（函数），表达式内容根据参数可变
    '''
    return lambda y: y ** x

def test():
    # 生成一个列表（可迭代对象）
    list_a = list(range(10))

    # 对列表作用func（一般函数）
    reslt = map(func,list_a)
    print(list(reslt))

    # 对列表作用func1（lambda表达式）
    func1 = lambda x : x * 2
    reslt = map(func1,list_a)
    print(list(reslt))

    # 对列表作用func2（lambda表达式，可变）
    func2 = lambda_func(3)
    reslt = map(func2,list_a)
    print(list(reslt))


def main():
    """
        主函数
    """
    test()

if __name__ == '__main__':
    main()
