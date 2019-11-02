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

COLOR = 0
# black and white
BW = 1
# binary
BINARY = 2

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
      dbg.dprintln(INFO, "writeImage() Writing BW file")
      path = "image/bw/" + str(filename)
      cv2.imwrite(path, image)
    elif type == BINARY:
      dbg.dprintln(INFO, "writeImage() Writing BINARY file")
      path = "image/binary/" + str(filename)
      cv2.imwrite(path, image)
    else:
      dbg.dprintln(INFO, "writeImage() Type is not BW or BINARY, not writing image")
  else:
    dbg.dprintln(INFO, "writeImage() .JPG extension not found in filename, not writing image")


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