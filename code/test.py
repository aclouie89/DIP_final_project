#!/usr/bin/python
# main
import cv2

# import retval
import retval as rv

# setup debug module
from debug import debug as dbg
CRITICAL = dbg.CRITICAL
INFO = dbg.INFO
VERBOSE = dbg.VERBOSE
ALL = dbg.ALL

# setup image module
from image import image_handler as imgh

from morph import morph as mo

#
# main function for testing
# EDIT ME
#
def main():
  dbg.enable()
  dbg.setLevel(dbg.ALL)
  dbg.dprintln(INFO, "test.py main() started")
  #
  # start test functions
  #

  # image handler testing
  # ./image or image all works
  [ret_val, image] = imghTest("./image/_raw/oscar_wilde_1.jpg")
  if ret_val == rv.SUCCESS:
    imghTest_write("test_image.jpg", image)

  ret_image = mo.erosion(image)
  imghTest_write("test_erosion_image.jpg", ret_image)
  ret_image = mo.dilation(image)
  imghTest_write("test_dilation_image.jpg", ret_image)
  ret_image = mo.open(image)
  imghTest_write("test_open_image.jpg", ret_image)
  ret_image = mo.close(image)
  imghTest_write("test_close_image.jpg", ret_image)

  #
  # end test functions
  #
  dbg.dprintln(INFO, "test.py main() ended")

##########
# image handler testing
#########
# testing exists & reading
def imghTest(img_path):
  image = None
  dbg.dprintln(VERBOSE, "imghTest() img_path = " + img_path, 1)
  # test case 1: check if file exists (THIS CHECKS FROM OUR CURRENT PATH)
  ret_val = imgh.imageExists(img_path)
  dbg.dprintln(INFO, "imghTest() image_exists() = " + rv.getRetString(ret_val), 1)
  # test case 2: convert image to grayscale
  if ret_val == rv.SUCCESS:
    [ret_val, image] = imgh.readImageGrayscale(img_path)
  return [ret_val, image]

# testing writes
def imghTest_write(filename, image):
  BW = imgh.BW
  BINARY = imgh.BINARY
  dbg.dprintln(VERBOSE, "imghTest_Write() writing image", 1)
  imgh.writeImage(BW, filename, image)



##########
# call main for testing
#########
main()