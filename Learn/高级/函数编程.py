
def addf(a,b,f):
    # f 是传入的函数参数
    return f(a,b) + f(b,a)

def func(a,b):
    '''
        作为参数的函数
    '''
    return a ** b

def test():
     print(addf(3, 5, func))


def main():
    """
        主函数
    """
    test()

if __name__ == '__main__':
    main()
