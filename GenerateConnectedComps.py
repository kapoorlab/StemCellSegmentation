
def ConnecProbability(img, minsize):
      
      binary  =  img > 0
     
      labels, nr_objects = ndimage.label(binary > 0) 
      nonormimg = fill_label_holes(labels[:,:] )
      nonormimg = remove_small_objects(nonormimg, min_size=minsize, connectivity=4, in_place=False)
      min = np.amin(nonormimg)
      max = np.amax(nonormimg)
      nonormimg = normalizeMinMax(nonormimg, min, max) 
        
      labels = nonormimg
      return labels
    
    