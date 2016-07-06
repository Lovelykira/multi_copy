import time
import random
from multiprocessing import Pool
import json
import os
import shutil

from functools import partial


SETTINGS_FILE = 'settings'


def copy_file( src_dir, dst_dir,file):
    print("Copying",file,"...")
    src = os.path.join(src_dir, file)
    dst = os.path.join(dst_dir, file)

    shutil.copyfile(src, dst)


if __name__ == '__main__':

    with open(SETTINGS_FILE) as f:
        num_processes = json.load(f)['num_processes']

    src_dir = input("Enter the source path: ")
    dst_dir = input("Enter the destination path: ")

    source_files = [f for f in os.listdir(src_dir)
                        if os.path.isfile(os.path.join(src_dir, f))]

    pool = Pool(num_processes)
    pool.map(partial(copy_file,src_dir, dst_dir),source_files)
    pool.close()
    pool.join()
    print("All Done")


