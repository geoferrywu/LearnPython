"""
    功能1：密码强度判断
    知识点1：str.isnumeric() str.isalpha() str.islower() str.isupper() isxxx..()

    功能2：输错次数限制，中止循环
    知识点2:continue bread

    功能3,4：保存密码，读取密码
    知识点3:文件操作
        open(filename, mode)
            mode:r/w/a/r+
            write()
            writelines() 写字符串列表

            read()
            readline()
        close()
    功能5：相关方法封装成整体，定义password工具类
    知识点：OOP
        class ClassName()
        class ClassName(SuperClassName) 继承
        def __init__(self) 构造函数
    功能6：相关方法封装成整体，定义文件操作类
"""


class PasswordTool:
    """
        密码工具类
    """
    def __init__(self, password):
        # 类的属性
        self.password = password
        self.strength_level = 0

    def process_password(self):
        # 规则1 密码长度大于8
        if len(self.password) >= 8:
            self.strength_level += 1
        else:
            print('密码长度要求至少8位')

        # 规则2 要有数字
        if self.check_number_exist():
            self.strength_level += 1
        else:
            print('密码要求包含数字')

        # 规则3 要有字母
        if self.check_letter_exist():
            self.strength_level += 1
        else:
            print('密码要求包含字母')

    # 类的方法
    def check_number_exist(self):
        """
                判断子字符串中是否有数字
        """
        has_number = False
        for c in self.password:
            if c.isnumeric():
                has_number = True
                break
        return has_number

    def check_letter_exist(self):
        """
                判断子字符串中是否有字母
        """
        has_letter = False
        for c in self.password:
            if c.isalpha():
                has_letter = True
                break
        return has_letter


class FileTool:
    """
        文件工具类
    """
    def __init__(self, filepath):
        self.filepath = filepath

    def write_to_file(self, line):
        f = open(self.filepath, 'a')
        f.write(line)
        f.close()

    def read_from_file(self):
        f = open(self.filepath, 'r')
        lines = f.readlines()
        f.close()
        return lines


def main():
    """
        主函数
    """
    try_times = 5
    times = 1

    # 实例化文件工具类
    filepath = 'password_3.0.txt'
    file_tool = FileTool(filepath)

    while times <= try_times:
        password = input('请输入密码(第{}次)：'.format(times))
        times += 1

        # 实例化对象
        password_tool = PasswordTool(password)
        password_tool.process_password()

        # 写文件
        line = '密码：{}，强度:{}\n'.format(password, str(password_tool.strength_level))
        file_tool.write_to_file(line)

        if password_tool.strength_level == 3:
            print('密码强度合格')
            break
        else:
            print('密码强度不合格')

        print()

    if times > try_times:
        print('错误次数过多！')

    # 读操作
    lines = file_tool.read_from_file()
    print(lines)


if __name__ == '__main__':
    main()
