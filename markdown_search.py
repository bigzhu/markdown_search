#!/usr/bin/env python
# encoding=utf-8
'''
hugo 中用来查找 wiki 词
'''
import fnmatch
import sys
import os
import time
try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except NameError:
    pass


RESULT_FILE = 'search.md'

NOT_IN = [RESULT_FILE, ".git", "assets", ".gitign"]


def search(path, name, not_in=[], sub_path=""):
    path = os.path.expanduser(path)  # 把 ~展开
    mds = {}
    sub_mds = {}
    file_path = path+sub_path
    for md in os.listdir(file_path):
        md = os.path.basename(md)
        if md in NOT_IN + not_in:  # 跳过目录特定文件名
            continue
        if os.path.isdir(file_path + md):  # 递归查找子目录
            sub_mds = search(path, name, not_in, sub_path + md + "/")
            mds.update(sub_mds)
            continue

        if(fnmatch.fnmatchcase(md.upper(), ('*%s*' % name).upper())):
            # 取文件修改时间
            modify_time = time.localtime(os.path.getmtime(file_path + md))
            no_suffix_md = md[:-3]
            mds[sub_path + no_suffix_md] = modify_time  # 子目录的文件, 要带上相对路径
        # 按时间排序
    mds = sorted(mds.items(), key=lambda by: by[1], reverse=True)
    return mds


def write(path, name, mds):
    '''
    '''
    path = os.path.expanduser(path)  # 把 ~展开
    f = open(path + RESULT_FILE, 'w')
    # print >>f, '%nohtml'
    for md in mds:
        # print >>f, '%s' % md[0]
        f.writelines(md[0] + '\n')
    f.writelines("tips/" + name + '\n')
    f.close()


def main():
    args = sys.argv
    if(len(args) == 1):
        print('请输入要查找的目录和 wiki 关键字')
        exit()
    elif(len(args) == 2):
        print('请输入要查找的目录和 wiki 关键字')
        exit()
    elif(len(args) == 3):
        path = args[1]
        name = args[2]
        mds = search(path, name)
        write(path, name, mds)


if __name__ == '__main__':
    main()
