import re

def test():
    s='''aaa=
ccc=eee
;sdfd=dfs
ddd=ggsdf
;
=
'''
    
    patt= r'^((?![;]).+=.*)$'   #寻找不以[]中的字符开头，且包含=的行
    p_multi=re.compile(patt, re.MULTILINE)
    pp = p_multi.findall(s)
    print(pp)

def main():
    """
        主函数
    """
    test()

if __name__ == '__main__':
    main()
    