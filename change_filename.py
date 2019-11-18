# -*- coding: utf-8 -*-
# @Time : 2019/11/18 23:34
# @Author : wangmengmeng
import os


def change_filename(path):
    filenames = os.listdir(r'E:\aa')
    print(filenames)
    i = 1
    for filename in filenames:
        oldF = os.path.join(path, filename)
        newF = os.path.join(path, str(i)+'.dat')
        os.rename(oldF, newF)
        i += 1
    filenames = os.listdir(r'E:\aa')
    print(filenames)


if __name__ == '__main__':
    path = r'E:\aa'
    change_filename(path)
