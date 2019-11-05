#!/usr/bin/python
# main
import cv2
import argparse
import config as cfg
from util import arg_parse_helper as aph

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
  # construct the argument parser and parse the arguments
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--image", type=str,
    help="path to input image")
  ap.add_argument("-c", "--conversion", type=aph.conversion2int, default=cfg.CONVERSION_ARG_BW,
    help="intermediate image conversion: 'bw' or 'bin'; defaults to 'bw'")
  ap.add_argument("-t", "--threshold", type=int,
    help="define an integer threshold for bimodal image conversion: (0-255)")
  ap.add_argument("-m", "--morph", type=aph.morph2int,
    help="define a morphological operation: 'erode', 'dilate', 'open' or 'close'")
  ap.add_argument("--invert", type=aph.str2bool, default=False,
    help="invert image?:'t' or 'f'; defaults to False")
  
  args = vars(ap.parse_args())

  # load the input image 
  [ret_val, image] = imghTest(args["image"])
  if ret_val == rv.SUCCESS:
    # TESTING GRAYSCALE DISCRETATION AND BIMODAL IMAGES
    
    intermediate_image = None

    if args["conversion"] == cfg.CONVERSION_ARG_BW:
      # discrete grayscale image
      imgh.writeImage(imgh.BW, "test_image_discretegrayscale.jpg", image)

      # inverted test
      if args["invert"]:
        intermediate_image = imgh.invert(image)
        imgh.writeImage(imgh.BW, "test_image_inverted_discretegrayscale.jpg", intermediate_image)
    
    elif args["conversion"] == cfg.CONVERSION_ARG_BIN:
      if args["threshold"]:
        # user defined threshold image + threshold value
        [intermediate_image, user_threshold] = imgh.imageToBimodal(imgh.USER_THRESH, image, args["threshold"])
        imgh.writeImage(imgh.BIN, "test_image_bimodal_user.jpg", intermediate_image)
      else:
        # global defined threshold image + global threshold value
        [intermediate_image, global_threshold] = imgh.imageToBimodal(imgh.GLOBAL_THRESH, image)
        imgh.writeImage(imgh.BIN, "test_image_bimodal_global.jpg", intermediate_image)

    # TEST MORPHOLOGIES
    # erosion

    if not args["morph"]:
      dbg.dprintln(INFO, "No morphological operation defined; operation will not be applied to image")
    else:
      if args["morph"] == cfg.MORPH_ARG_ERODE:
        ret_image = mo.erode(intermediate_image, 1 )
        imgh.writeImage(imgh.BIN, "test_image_bimodal_user_erode.jpg", ret_image)
      elif args["morph"] == cfg.MORPH_ARG_DILATE:
        ret_image = mo.dilate(intermediate_image, 1 )
        imgh.writeImage(imgh.BIN, "test_image_bimodal_user_dilation.jpg", ret_image)
      elif args["morph"] == cfg.MORPH_ARG_OPEN:
        ret_image = mo.open(intermediate_image, 1 )
        imgh.writeImage(imgh.BIN, "test_image_bimodal_user_open.jpg", ret_image)
      elif args["morph"] == cfg.MORPH_ARG_CLOSE:
        ret_image = mo.close(intermediate_image, 1 )
        imgh.writeImage(imgh.BIN, "test_image_bimodal_user_close.jpg", ret_image)

    # TEST 

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
  image_path = img_path

  # load default image if image is left blank
  if not img_path:
    dbg.dprintln(INFO, "NO IMAGE PATH SPECIFIED, LOADING DEFAULT IMAGE: " + cfg.DEFAULT_IMAGE_PATH)
    image_path = cfg.DEFAULT_IMAGE_PATH

  dbg.dprintln(VERBOSE, "imghTest() image_path = " + image_path, 1)
  
  # test case 1: check if file exists (THIS CHECKS FROM OUR CURRENT PATH)
  ret_val = imgh.imageExists(image_path)
  dbg.dprintln(INFO, "imghTest() image_exists() = " + rv.getRetString(ret_val), 1)
  # test case 2: convert image to grayscale
  if ret_val == rv.SUCCESS:
    [ret_val, image] = imgh.readImageGrayscale(image_path)
  elif ret_val == rv.ERROR_NO_FILE:
    dbg.dprintln(INFO, "NO FILE AT SPECIFIED PATH")
  elif ret_val == rv.ERROR_NO_IMAGE:
    dbg.dprintln(INFO, "NO IMAGE AT SPECIFIED PATH")
  return [ret_val, image]


##########
# call main for testing
#########
main()