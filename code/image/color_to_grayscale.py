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
sys.path.append(os.path.abspath('../debug'))
import debug as dbg

# set debug constants
CRITICAL = dbg.CRITICAL
INFO = dbg.INFO
VERBOSE = dbg.VERBOSE
ALL = dbg.ALL

dbg.dprintln(INFO, "Starting color_to_grayscale.py")
## load user arguments ##
try:
    #argv[0] = this python's file name
    INPUT_ARGS = str(sys.argv[1])
except IndexError:
  dbg.dprintln(CRITICAL, '\tUSER INPUT ERROR: Missing cmd line argument(s)', 1)
  sys.exit(0)

if len(INPUT_ARGS) > 1:
  # get filename
  print("ARGS: " + str(INPUT_ARGS))
  ARGS_INPUT_FILE = INPUT_ARGS
else:
  dbg.dprintln(CRITICAL, "No input image file specified", 1)
  sys.exit(0)

if ARGS_INPUT_FILE is not None:
  dbg.dprintln(INFO, "Processing image: " + ARGS_INPUT_FILE, 1)
  # convert image to grayscale
  image_gray = cv2.imread(ARGS_INPUT_FILE, cv2.IMREAD_GRAYSCALE)
  OUTPUT_FILE = "bw_" + INPUT_ARGS[4:]
  # output a grayscale image
  cv2.imwrite(OUTPUT_FILE, image_gray)



dbg.dprintln(INFO, "Ending color_to_grayscale.py")