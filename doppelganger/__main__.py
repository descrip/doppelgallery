import openface
import os
from image_db import ImageDB
from get_rep import getRep
from parse_imgs import dir_to_rep

if __name__ == "__main__":
    idb = dir_to_rep("/root/images/train_1/")
    idb.save_to_file("test_save")

    idb2 = ImageDB()
    idb2.load_from_file("test_save")
    print(idb2)
