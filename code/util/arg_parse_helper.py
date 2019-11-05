import argparse
import sys
sys.path.append("..")
import config as cfg

## for parsing boolean arguments
def str2bool(v):
  if isinstance(v, bool):
    return v
  if v.lower() in ('yes', 'true', 't', 'y', '1'):
    return True
  elif v.lower() in ('no', 'false', 'f', 'n', '0'):
    return False
  else:
    raise argparse.ArgumentTypeError('Boolean value expected.')

## for parsing intermediate image conversion arguments
def conversion2int(v):
  if v.lower() == "bw":
    return cfg.CONVERSION_ARG_BW
  elif v.lower() == "bin":
    return cfg.CONVERSION_ARG_BIN
  else:
    raise argparse.ArgumentTypeError('Invalid image conversion.')

## for parsing morphological operation arguments
def morph2int(v):
  if v.lower() == "erode":
    return cfg.MORPH_ARG_ERODE
  elif v.lower() == "dilate":
    return cfg.MORPH_ARG_DILATE
  elif v.lower() == "open":
    return cfg.MORPH_ARG_OPEN
  elif v.lower() == "close":
    return cfg.MORPH_ARG_CLOSE
  else:
    raise argparse.ArgumentTypeError('Invalid morphological operation.')