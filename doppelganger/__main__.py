import openface
import os
import sys
from image_db import ImageDB
from get_rep import getRep
from parse_imgs import dir_to_rep


def get_nearest(fname):
    idb = ImageDB()
    idb.load_from_file("test_save")

    mat = getrep(fname)
    dists, names = idb.k_nearest(mat,4)
    print(dists)
    print(names)
    return dists, names

# test_save is /root/data/mattest_save and /root/data/namestest_save
# function loads the directory dirname and saves it into an ImageDB format
def load_dir(dirname):
    idb = ImageDB()
    idb.load_from_vecs(dirname)
    idb.save_to_file("test_save")
    return None

# takes an input directory and prints processed images to /root/data/out
def convert_dir():
    dir_to_rep(sys.argv[1])
    return None

if __name__ == "__main__":
    # dir_to_rep(sys.argv[1])
