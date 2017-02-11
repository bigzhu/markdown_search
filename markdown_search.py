#!/usr/bin/env python
# encoding=utf-8
'''
vimwiki 中用来查找 wiki 词
'''
import fnmatch
import sys
import os
import time

reload(sys)
sys.setdefaultencoding('utf-8')

RESULT_FILE = 'search.md'

NOT_IN = [RESULT_FILE]


def search(path, name):
    mds = {}
    for md in os.listdir(path):
        md = os.path.basename(md)
        if os.path.isdir(path + md):  # 跳过目录
            continue
        if md in NOT_IN:  # 跳过目录特定文件名
            continue

        if(fnmatch.fnmatchcase(md.upper(), ('*%s*' % name).upper())):
            # 取文件修改时间
            modify_time = time.localtime(os.path.getmtime(path + md))
            mds[md] = modify_time
        # 按时间排序
    mds = sorted(mds.items(), key=lambda by: by[1], reverse=True)
    return mds


def write(path, name, mds):
    '''
    '''
    f = open(path + RESULT_FILE, 'w')
    # print >>f, '%nohtml'
    for md in mds:
        print >>f, '%s' % md[0]
    print >>f, '%s.md' % name
    f.close()


def main():
    args = sys.argv
    if(len(args) == 1):
        print '请输入要查找的目录和 wiki 关键字'
        exit()
    elif(len(args) == 2):
        print '请输入要查找的目录和 wiki 关键字'
        exit()
    elif(len(args) == 3):
        path = args[1]
        name = args[2]
        mds = search(path, name)
        write(path, name, mds)

if __name__ == '__main__':
    main()
