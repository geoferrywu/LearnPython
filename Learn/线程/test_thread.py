
from threading import Thread
from threading import Event
import time


class Job(Thread):
    def __init__(self, *args, **kwargs):
        super(Job, self).__init__()
        self._name=args[0]      # Job Name
        self._timer=args[1]     # Job Timer
        self._stopJob = Event() # 用于停止线程的标识
        self._stopJob.clear()


    def run(self):
        t1 = t2 = time.time()
        self.__realWork(t1)
        while True:

            if t2 - t1 >= self._timer:
                t1 += self._timer
                self.__realWork(t2)
            else:
                time.sleep(0.001)
            t2 = time.time()

            if self._stopJob.is_set():
                print('子线程结束', self._name)
                break

    
    def __realWork(self,t):
        print(self._name,t)


    def terminate(self):
        self._stopJob.set()


def test():
    # 创建两个线程
    J1 = Job('J1',1)
    J2 = Job('J2',2)
    try:
        t = time.time()
        t2 = time.time()
        print('主线程', t)

        J1.start()
        J2.start()
        # 主线程运行10s
        while t2 - t <= 10:
            time.sleep(0.05)
            t2 = time.time()

        print('主线程结束', t2)

        J1.terminate()
        J2.terminate()

    except:
        print("Error: unable to start thread") 
    

def main():
    """
        主函数
    """
    test()

if __name__ == '__main__':
    main()
