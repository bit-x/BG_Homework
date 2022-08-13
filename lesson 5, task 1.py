import os
import sys

def mk_dir (path):
    os.mkdir(path)

def rm_dir (path):
    os.removedirs(path)

if __name__ == "__main__":
    dir_parh = 'dir_{}'
    [mk_dir(dir_parh.format(i)) for i in range(1, 10)]
    [rm_dir(dir_parh.format(i)) for i in range(1, 10)]