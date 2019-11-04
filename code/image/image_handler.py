#!/usr/bin/python
# usage:
#   python3 color_to_grayscale.py raw/oscar_wilde_1.jpg
# restrictions:
#   only converts jpg
#   invalid files/paths will not cause an error the result file will be empty instead

import cv2
import os
import sys

# import the debug module
sys.path.append(os.path.abspath('../'))
from debug import debug as dbg

# set debug constants
CRITICAL = dbg.CRITICAL
INFO = dbg.INFO
VERBOSE = dbg.VERBOSE
ALL = dbg.ALL

# import the return value module
import retval

################
# Image types
################
COLOR = 0
# Discrete grayscale
BW = 1
# bimodal
BIN = 2


################
# Thresholding types
################
NO_THRESH = 0
# user defined value
USER_THRESH = 1
# global threshold
GLOBAL_THRESH = 2
# adaptive mean thresholding
MEAN_THRESH = 3
# adaptive gaussian thresholding
GAUSS_THRESH = 4


###################
# user thresholding - private do not call
###################
# user set thresholding
def userThresholding(image, threshold):
  new_image = image.copy()
  for row in range(new_image.shape[0]):
    for col in range(new_image.shape[1]):
      if new_image[row][col] >= threshold:
        new_image[row][col] = 255
      else:
        new_image[row][col] = 0
  return new_image

###################
# global thresholding - private do not call
###################
# compute the histogram
def compute_histogram(image):
    hist = [0]*256
    for row in range(image.shape[0]):
        for col in range(image.shape[1]):
            pixel_val = image[row, col]
            if pixel_val >= 0 and pixel_val < 256:
                hist[pixel_val] = hist[pixel_val] + 1
            else:
                dbg.dprintln(CRITICAL, "Found erroneous pixel value: " + str(pixel_val) + " at " + str(row) + ", " + str(col), 2)
    return hist

# find the optimal threshold
def find_optimal_threshold(hist):
    # init counters
    max_lo = 0
    max_hi = 0
    lo_cnt = 0
    hi_cnt = 0
    # init threshold
    threshold = len(hist) // 2
    # find the avg prob val before and after threshold
    for x in range(len(hist)):
        if x < threshold:
            max_lo = max_lo + x * hist[x]
            lo_cnt = lo_cnt + hist[x]
        else:
            max_hi = max_hi + x * hist[x]
            hi_cnt = hi_cnt + hist[x]
    # calc threshold value
    max_lo = max_lo // lo_cnt
    max_hi = max_hi // hi_cnt
    threshold = (max_lo + max_hi) // 2
    dbg.dprintln(VERBOSE, "Threshold value is: " + str(threshold) + " with maximas: " + str(max_lo) + ", " + str(max_hi), 2)
    return threshold

# global thresholding
def globalThresholding(image):
  new_image = image.copy()
  threshold = find_optimal_threshold(compute_histogram(new_image))
  dbg.dprintln(VERBOSE, "Threshold is: " + str(threshold), 2)
  for row in range(new_image.shape[0]):
      for col in range(new_image.shape[1]):
          if new_image[row, col] >= threshold:
              new_image[row, col] = 255
          else:
              new_image[row, col] = 0
  return [new_image, threshold]


###################
# PUBLIC FUNCTIONS
###################
# converts a color image to grayscale
# Input:
#   abs_image_path: (STRING) ABSOLUTE image path
#   binarize: (BOOL) default value false for no binarization
# Output:
#   (cv2 image) grayscale or binary image matrix
def readImageGrayscale(abs_image_path, binarize=False):
  if abs_image_path is not None:
    # success
    if imageExists(abs_image_path) == retval.SUCCESS:
      image = cv2.imread(abs_image_path, cv2.IMREAD_GRAYSCALE)
      return [retval.SUCCESS, image]
    # bad file path
    else:
      dbg.dprintln(CRITICAL, "readImageGrayscale() invalid image path, no file found")
      return [retval.ERROR_NO_FILE, None]
  # bad input argument abs_image_path
  else:
    dbg.dprintln(CRITICAL, "readImageGrayscale() no image path defined")
    return [retval.ERROR_NO_IMAGE, None]

# writes a BW or BINARY image matrix to a file
# Input:
#   image: (numpy matrix) image matrix
#   type: (INT) where to write it to
def writeImage(type, filename, image):
  if(".jpg" in str(filename)):
    if type == BW:
      dbg.dprintln(INFO, "writeImage() Writing BW file", 1)
      path = "image/bw/" + str(filename)
      cv2.imwrite(path, image)
    elif type == BIN:
      dbg.dprintln(INFO, "writeImage() Writing BINARY file", 1)
      path = "image/binary/" + str(filename)
      cv2.imwrite(path, image)
    else:
      dbg.dprintln(INFO, "writeImage() Type is not BW or BINARY, not writing image", 1)
  else:
    dbg.dprintln(INFO, "writeImage() .JPG extension not found in filename, not writing image", 1)

# returns a bimodal image
# Input:
#   type: (INT) check THRESHOLDING TYPES above
#   image: (numpy matrix) image matrix
#   threshold: (INT) threshold value
def imageToBimodal(type, image, threshold=127):
  dbg.dprintln(INFO, "imageToBimodal(): threshold specified " + str(threshold))
  # invalid threshold value, return
  if threshold < 0 or threshold > 255:
    dbg.dprintln(CRITICAL, "Invalid threshold value: " + str(threshold), 1)
  # check for type and return the threshold
  elif type == NO_THRESH:
    dbg.dprintln(INFO, "No threshold, returning raw image untouched", 1)
  # user specified bimodal threshold
  elif type == USER_THRESH:
    dbg.dprintln(INFO, "User threshold specified " + str(threshold), 1)
    image = userThresholding(image, threshold)
  # global threshold
  elif type == GLOBAL_THRESH:
    dbg.dprintln(INFO, "Global threshold, automatically finding optimal threshold based on histogram")
    [image, threshold] = globalThresholding(image)
  # not yet implemented
  else:
    dbg.dprintln(CRITICAL, "Thresholding mode has no valid implementation")
  return [image, threshold]


# checks if file exists
# Input:
#   abs_image_path: (STRING) ABSOLUTE image path
# Output:
#   retval
def imageExists(abs_image_path):
  if os.path.exists(abs_image_path):
    return retval.SUCCESS
  else:
    return retval.ERROR_NO_FILE