"""
    根据图像文件修改日期，移动到各个日期目录下
"""

import os
import time
import shutil

# 图像文件扩展名
imageExt = ['.jpg','.bmp','.png','.mp4','.mov']

def makeImageDict(fold):
    '''
        指定目录下的文件生成 日期:[文件名,文件名,文件名...]的字典
    '''
    img_dict = dict()
    files_and_dirs = os.listdir(fold)
    for fname in files_and_dirs:
        # 只列出符合条件的文件
        if os.path.isfile(os.path.join(fold, fname)) and \
           os.path.splitext(fname)[1] in imageExt:
            imgDate = time.localtime(os.path.getmtime(os.path.join(fold, fname)))
            datestr = time.strftime('%Y%m%d', imgDate)

            if datestr not in img_dict.keys():
                img_dict[datestr] = list()
            img_dict[datestr].append(fname)
    
    return img_dict


def move_images(rootFold,img_dict):
    '''
        移动文件到日期目录下
    '''
    for key,value in img_dict.items():
        newFold = os.path.join(rootFold,key)
        if not os.path.isdir(newFold):
            '建目录'
            os.mkdir(newFold)
        for img in value:
            shutil.move(os.path.join(rootFold,img),newFold)



def classify_by_time(rootFold):
    '''
        指定目录下的图像文件，移动到对应修改日期的目录下
    '''
    img_dict = makeImageDict(rootFold)
    move_images(rootFold, img_dict)

def main():
    """
        主函数
    """
    rootFold = 'D:\\刚手机20190415迄'
    classify_by_time(rootFold)


if __name__ == '__main__':
    main()
