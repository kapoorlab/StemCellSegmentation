import sys
sys.path.insert(0, "/data/u934/service_imagerie/v_kapoor/anaconda2/bin/PyImage/utils")
from scipy import ndimage
from stardist import fill_label_holes
import scipy
import numpy as np
from skimage import measure
from skimage import filters
from skimage.segmentation import find_boundaries,find_boundaries, relabel_sequential
from skimage.morphology import remove_small_objects, binary_erosion
from skimage.filters import threshold_otsu, threshold_mean
from skimage.exposure import rescale_intensity
from Normalize import Path,normalizeMinMax

def ConnecProbability(img, minsize):
      
      thresh = threshold_mean(img)
      binary  =  img > thresh
      binary = binary_erosion(binary)  
      binary = fill_label_holes(binary[:,:] )
      labels, nr_objects = ndimage.label(binary > 0) 
      nonormimg = fill_label_holes(labels[:,:] )
      nonormimg = remove_small_objects(nonormimg, min_size=minsize, connectivity=4, in_place=False)
      nonormimg, forward_map, inverse_map = relabel_sequential(nonormimg) 
      
      labels = nonormimg
      return labels
    
    