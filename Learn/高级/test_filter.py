"""
    求素数
"""

def _odd_iter():
    '''
        先构造一个从3开始的奇数序列
        这是一个生成器，并且是一个无限序列
    '''
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    '''
        定义一个筛选函数，去掉能被n整除的数
    '''
    return lambda x: x % n > 0

def primes():
    '''
        定义一个生成器，不断返回下一个素数
    '''
    yield 2
    it = _odd_iter() # 初始序列，无限序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列,序列的第一个数就是素数


def not_empty(s):
    return s and s.strip()

list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))

def test():
    # 打印10以内的素数:
    for n in primes():
        if n < 10:
            print(n)
        else:
            break

    # 过滤非空及非None的列表元素
    list_b = ['A', '', 'B', None, 'C', '  ']
    rest = filter(lambda x: x and x.strip() !='', list_b)
    print(list(rest))

def main():
    """
        主函数
    """
    test()

if __name__ == '__main__':
    main()
