
class Student(object):
    stu_name = 'Student'
    def __init__(self):
        # 类内部变量
        self.name = 'name'
        self.score = 100

    def use_var(self):
        print(self.name)
        print(Student.stu_name)
            

def test():
    stu= Student()
    # 给类实例增加变量
    stu.name2 = 'sfsfs'
    Student.use_var(stu)
    #print(stu.stu_name,stu.name2,stu.stu_name)
    stu.use_var() 
   

def main():
    """
        主函数
    """
    test()

if __name__ == '__main__':
    main()
