from get_rep import getRep
from image_db import ImageDB

def dir_to_rep(dir_path, verbose=True):
    idb = ImageDB()
    for filename in os.listdir(dir_path):
        if filename.endswith(".jpg"):
            file_location = os.path.join(dir_path, filename)
            rep = getRep(file_location)
            if rep is not None:
                idb.add_img(rep, file_location)

            else:
                print("%s did not have any recognized faces in it." % filename)


    idb.save_to_file("test_idb_storage")
