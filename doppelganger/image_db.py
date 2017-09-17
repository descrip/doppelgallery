import numpy as np


# implement image class? class contains the img_mat, and a vector of image names

class ImageDB:
    def __init__(self, img_mat=[], img_names=[]):
        self.img_mat = img_mat
        self.img_names = img_names

    def add_img(self, img_vec, img_name):
        self.img_mat = np.vstack((self.img_mat,img_vec))
        self.img_names = np.append(img_names, img_name)

    # assumes img_mat is an n * 128 numpy matrix of image references, n>=4
    # assumes input_img is a [128] numpy vector representing the image
    def k_nearest(self, input_img, k):
        vec_diff = self.img_mat - input_img
        dists = np.square(np.einsum('ij,ij->i', vec_diff, vec_diff))
        idx = np.argpartition(dists,k)
        return dists[idx[:k]], idb.get_img_names(idx[:k])

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




