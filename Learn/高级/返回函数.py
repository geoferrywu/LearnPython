"""
    求和及延迟求和
"""

def calc_sum(*args):
    '''
        普通求和
    '''
    ax = 0
    for n in args:
        ax = ax + n
    return ax

def lazy_sum(*args):
    '''
        延迟求和，返回求和函数
    '''
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


def createCounter():
    '''
        形成闭包，n被打包到返回函数中去
    '''
    n = 0
    def counter():
        nonlocal n # 使用外层变量
        n += 1
        return n
    return counter

def createCounter2():
    def _num_iter():
        '''
            先构造一个从1开始的自然数序列
            这是一个生成器，并且是一个无限序列
        '''
        n = 0
        while True:
            n += 1
            yield n

    it = _num_iter()

    def counter():
        return next(it)
    
    return counter


def test():
    print('lazy_sum求和')
    f = lazy_sum(1, 3, 5, 7, 9)
    print(f())

    counterA = createCounter()
    counterB = createCounter()  #counterB和counterA是2个函数，内部变量是独立的
    # 目的：每次调用递增1
    print('counterB和counterA是2个函数，内部变量是独立的')
    print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
    print(counterB(), counterB(), counterB(), counterB(), counterB()) # 1 2 3 4 5

    counterA = createCounter()
    counterB = counterA  #counterB和counterA是1个函数，内部变量是同一个
    # 目的：每次调用递增1
    print('counterB和counterA是1个函数，内部变量是同一个')
    print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
    print(counterB(), counterB(), counterB(), counterB(), counterB()) # 1 2 3 4 5

    counterA = createCounter2()
    # 目的：每次调用递增1
    print('使用生成器')
    print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5


def main():
    """
        主函数
    """
    test()

if __name__ == '__main__':
    main()
