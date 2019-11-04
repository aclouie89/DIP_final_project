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
  # SET DEBUG LEVEL
  dbg.setLevel(ALL)
  dbg.dprintln(INFO, "test.py main() started")
  #
  # start test functions
  #

  # image handler testing
  # ./image or image all works
  [ret_val, image] = imghTest("./image/_raw/oscar_wilde_1.jpg")
  if ret_val == rv.SUCCESS:
    # TESTING GRAYSCALE DISCRETATION AND BIMODAL IMAGES
    # discrete grayscale image
    imgh.writeImage(imgh.BW, "test_image_discretegrayscale.jpg", image)
    # user defined threshold image + threshold value
    [user_image, user_threshold] = imgh.imageToBimodal(imgh.USER_THRESH, image, 220)
    imgh.writeImage(imgh.BIN, "test_image_bimodal_user.jpg", user_image)
    # global defined threshold image + global threshold value
    [global_image, global_threshold] = imgh.imageToBimodal(imgh.GLOBAL_THRESH, image)
    imgh.writeImage(imgh.BIN, "test_image_bimodal_global.jpg", global_image)

    # TEST MORPHOLOGIES
    # erosion
    ret_image = mo.erode(user_image, 1 )
    imgh.writeImage(imgh.BIN, "test_image_bimodal_user_erode.jpg", ret_image)
    ret_image = mo.dilate(user_image, 1 )
    imgh.writeImage(imgh.BIN, "test_image_bimodal_user_dilation.jpg", ret_image)
    ret_image = mo.open(user_image, 1 )
    imgh.writeImage(imgh.BIN, "test_image_bimodal_user_open.jpg", ret_image)
    ret_image = mo.close(user_image, 1 )
    imgh.writeImage(imgh.BIN, "test_image_bimodal_user_close.jpg", ret_image)

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



##########
# call main for testing
#########
main()