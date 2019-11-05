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
  # get unique list of morph args
  arg_list = list(set([arg.strip() for arg in v.split(',')]))

  morph_dict = {
    "erode": cfg.MORPH_ARG_ERODE,
    "dilate": cfg.MORPH_ARG_DILATE,
    "open": cfg.MORPH_ARG_OPEN,
    "close": cfg.MORPH_ARG_CLOSE
  }

  return ([morph_dict[arg] if arg in morph_dict else morphException()
    for arg in arg_list])

def morphException():
  raise argparse.ArgumentTypeError('Invalid morphological operation.')

