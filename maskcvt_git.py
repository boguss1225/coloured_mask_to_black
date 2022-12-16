from PIL import Image
#import numpy as np
#from mxnet import gluon, np, image, npx
import cv2
import numpy
import glob
import sys
import numpy as np
import os
np.set_printoptions(threshold=sys.maxsize)

path = '/Users/bogus/Downloads/SegmentationClass/' # Source Folder
dstpath = '/Users/bogus/Downloads/SegmentationClass2/' # Destination Folder

#color mapping
VOC_COLORMAP = [[176, 112, 32], [48, 240, 32], [48, 112, 32], [176, 240, 160],
                [176, 240, 32], [48, 240, 160], [176, 112, 160]]

#@save
VOC_CLASSES = ['background', 'hyperthalamus', 'cerebral', 'thalamus', 
               'hippo', 'soma', 'audi']

#@convert & save
def convert_to_iii(file_dir):
    """Build an RGB color to label mapping for segmentation."""
    im=cv2.imread(file_dir)
    print("im",im[1,1])
    for i, colormap in enumerate(VOC_COLORMAP):
        # print(i,".",VOC_CLASSES[i],":",colormap[0],"-",colormap[1],"-",colormap[2])
        im[np.where((im == [colormap[2],colormap[1],colormap[0]]).all(axis = 2))] = [i,i,i]
    filename = os.path.split(file_dir)[-1]
    cv2.imwrite((os.path.join(dstpath,filename)),im)

#@iterate folder
def voc_label_indices(folder_dir):
    explore_path = folder_dir + "/*.png"
    path_list = glob.glob(explore_path)
    print(explore_path)
    print("len",len(path_list))
    for file_dir in path_list:
        print(file_dir)
        convert_to_iii(file_dir)

copy_bool = input("Copy target directory before excute. Excute? (Y/N):")

if copy_bool=='y' or copy_bool=='Y':
    print("Start conversion")
    voc_label_indices(path)
    print("Done")
else : 
    print("See you")
