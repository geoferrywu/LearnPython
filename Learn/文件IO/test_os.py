import os
import glob # 文件名模式匹配库

def test_os():
    cwd = os.getcwd()
    print('当前工作目录:', cwd)

    execpath = os.get_exec_path()
    print('exec_path:', execpath)

    login = os.getlogin()
    print('login name:', login)

    cur_dir = os.path.dirname(__file__)
    print('当前文件所在目录:', cur_dir)
    
    try:
        newdir = cur_dir + '\\test\\test'
        if os.path.isdir(newdir):
            os.rmdir(newdir)
            print(newdir + ' removed.')
        os.mkdir(newdir)
        print(newdir + ' created.')
    finally:
        pass


def test_walk():
    '''
       遍历目录（所有子目录及文件）
    '''
    rootdir = 'D:\\HYRON_input_AI_190308\\FZ-Application\\FZ_FH_FJ-XXX.610'
    for root, dirs, files in os.walk(rootdir, topdown=True):
        print('root is:', root)
        for name in files:
            print(name)
        for dir in dirs:
             print(dir)


def test_list():
    rootdir = 'D:\\HYRON_input_AI_190308\\FZ-Application\\FZ_FH_FJ-XXX.610\\'
    files_and_dirs = os.listdir(rootdir)
    for name in files_and_dirs:
        # 只列出文件
        if os.path.isfile(rootdir + name):
            print(name)
    

def test_glob():
    rootdir = 'D:\\HYRON_input_AI_190308\\FZ-Application\\FZ_FH_FJ-XXX.610\\Release_XP\\Message\\'
    filelist = glob.glob(rootdir + '*jpn.msg')
    for name in filelist:
        # if os.path.isfile(rootdir + name):
        print(name)
    # return filelist


def main():
    """
        主函数
    """
    # test_os()
    # test_walk()
    # test_list()
    test_glob()

if __name__ == '__main__':
    main()