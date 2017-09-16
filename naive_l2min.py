import numpy as np


# implement image class? class contains the img_mat, and a vector of image names

class ImageDB:
    def __init__(self, img_mat=[], img_names=[]):
        self.img_mat = img_mat
        self.img_names = img_names

    # assumes img_mat is an n * 128 numpy matrix of image references, n>=4
    # assumes input_img is a [128] numpy vector representing the image
    def k_nearest(self, input_img, k):
        vec_diff = self.img_mat - input_img
        dists = np.square(np.einsum('ij,ij->i', vec_diff, vec_diff))
        idx = np.argpartition(dists,k)
        return dists[idx[:k]], idx[:k]

    # prints out the images names given an index set
    def get_img_names(self, idx):
        return [self.img_names[x] for x in idx]

    # returns a string representation of the ImageDB
    def to_string(self):
        return self.img_mat.tostring(), "&&".join(self.img_names)

    # builds an ImageDB from a string pair
    def from_string_pair(self, mat_str, imname_str):
        self.img_mat = np.fromstring(mat_str, dtype=np.float).reshape(-1,3)
        self.img_names = imname_str.split("&&")
        return None

def idb_4nearest(idb, in_img):
    dists, indices = idb.k_nearest(in_img, 4)
    return dists, idb.get_img_names(indices)


if __name__ == "__main__":
    # example input
    img_mat = np.array([[1,2,3],[4,5,6],[0,1,0],[1,1,1],[3,5,9],[1,4,2]], dtype=np.float)
    img_names = ["pic_1","pic_large","pic_small","pic1","pic2","pic3"]

    # build the database
    idb = ImageDB(img_mat, img_names)

    # test conversion to string to build a copy
    str1, str2 = idb.to_string()
    idb2 = ImageDB()
    idb2.from_string_pair(str1, str2)

    # test input
    in_img = np.array([0,1,5])

    # print the 4 nearest elements along with their distances
    print(idb_4nearest(idb, in_img))



