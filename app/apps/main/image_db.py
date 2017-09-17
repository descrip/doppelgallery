import numpy as np
import os
from vars import DATA_DIR


# implement image class? class contains the img_mat, and a vector of image names

class ImageDB:
    def __init__(self, img_mat=[], img_names=[]):
        self.img_mat = img_mat
        self.img_names = img_names
        self.empty = True

    def __str__(self):
        return str(self.img_mat) + '\n' + str(self.img_names)


    def load_from_vecs(self, dir_path):
        # this is the largest size we would have to worry about
        total_files = len([name for name in os.listdir(dir_path)])
        self.img_mat = np.zeros((total_files,128))
        self.img_names = []
        ct = 0
        for filename in os.listdir(dir_path):
            mat = np.loadtxt(os.path.join(dir_path, filename))
            name_id = filename.split("_")[1].split(".")[0]
            if mat.size == 0:
                pass
            else:
                self.img_mat[ct] = mat
                self.img_names.append(name_id)
                ct += 1
        self.img_mat = self.img_mat[:ct]

    # assumes img_mat is an n * 128 numpy matrix of image references, n>=4
    # assumes input_img is a [128] numpy vector representing the image
    def k_nearest(self, input_img, k):
        vec_diff = self.img_mat - input_img
        dists = np.square(np.einsum('ij,ij->i', vec_diff, vec_diff))
        idx = np.argpartition(dists,k)
        return dists[idx[:k]], self.get_img_names(idx[:k])

    # prints out the images names given an index set
    def get_img_names(self, idx):
        return [self.img_names[x] for x in idx]

    def save_to_file(self, filename):
        np.save(DATA_DIR+'mat'+filename, self.img_mat)
        np.save(DATA_DIR+'names'+filename, self.img_names)
        return None

    def load_from_file(self, filename):
        self.img_mat = np.load(DATA_DIR + 'mat'+filename+'.npy')
        self.img_names = np.load(DATA_DIR + 'names'+filename+'.npy')
        return None




