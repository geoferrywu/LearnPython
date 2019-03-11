"""
    功能：BMR计算 V3.0
    知识点：字符串的分隔(split)及格式化(format)函数
"""


def main():
    """
        主函数
    """
    print('请输入以下信息，用[,]分隔。')
    info_str = input('性别,体重(kg),身高(cm),年龄\n')    # \n 表示换行
    info_list = info_str.split(',')
    weight = info_list[1]
    length = info_list[2]

    # {n}是format函数的占位标识，n可以表示format中数据的顺序，n从0开始可以省略
    print('体重是{0}公斤，身高{1}cm'.format(weight, length))


if __name__ == '__main__':
    main()
