import sys
from matplotlib import pyplot
from mtcnn import MTCNN
from PIL import Image
# load the photograph

def detect(pic):
    #im = Image.open('static/uploads/' + pic)
    pixels = pyplot.imread('static/uploads/' + pic)
    # create the detector, using default weights
    detector = MTCNN()
    # detect faces in the image
    try:
        faces = detector.detect_faces(pixels)
    except:
        print('Not a face')
        faces = 0
    return faces
