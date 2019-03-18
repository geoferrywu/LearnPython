"""
    log() 装饰函数
"""
import functools
import time

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            begin = time.time()
            r = func(*args, **kw)
            end = time.time()
            print('%s executed in %s ms' % (func.__name__, 1000 * (end - begin)))
            return r
        return wrapper
    return decorator

@log('')
def addf(a,b):
    return a+b

def test():
    print(addf(3,5))

def main():
    """
        主函数
    """
    test()

if __name__ == '__main__':
    main()
