from get_rep import getRep
from image_db import ImageDB
import os
import numpy as np

def dir_to_rep(dir_path, verbose=True):
    idb = ImageDB()
    total_files = len([name for name in os.listdir(dir_path)])
    counter = 0
    for filename in os.listdir(dir_path):
        counter += 1
        # print("Currently analysed %d of %d images." % (counter, total_files))
        if filename.endswith(".jpg"):
            file_location = os.path.join(dir_path, filename)
            outfile = os.path.join('/root/data/out/', 'npvec_'+filename.split(".")[0]+'.txt')
            if os.path.exists(outfile):
                pass
            else:
                rep = getRep(file_location)
                if rep is not None:
                    np.savetxt(outfile, rep)
                    # idb.add_img(rep, str(file_location))

                else:
                    np.savetxt(outfile, [])
                    # print("%s did not have any recognized faces in it." % filename)

    return None

