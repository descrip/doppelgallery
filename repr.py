import openface
align = openface.AlignDlib(args.dlibFacePredictor)
def getRep(imgPath):
    # load some image
    bgrImg = cv2.imread(imgPath)

    # couldn't load image
    if bgrImg is None:
        raise Exception("Unable to load image: {}".format(imgPath))

    # load some other image (rgb?)
    rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)

    # build the bounding box
    bb = align.getLargestFaceBoundingBox(rgbImg)

    # couldn't find a face, so we return none
    if bb is None:
        return None

    # build an aligned face
    alignedFace = align.align(args.imgDim, rgbImg, bb,
                              landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)

    # could not align face properly
    if alignedFace is None:
        return None
        # raise Exception("Unable to align image: {}".format(imgPath))

    # build the actual representation
    rep = net.forward(alignedFace)
    return rep
