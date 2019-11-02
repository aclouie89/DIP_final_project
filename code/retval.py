# global return standards

# general success
SUCCESS = 0
# general error
ERROR = 1
# err no file
ERROR_NO_FILE = 2
# err no image
ERROR_NO_IMAGE = 3

# STRING output for the above
RET_STRING = ["SUCCESS", "ERROR", "ERROR_NO_FILE", "ERROR_NO_IMAGE"]

# returns ret_string based on given index ret_val
# Input:
#   ret_val: (INT) index to ret_string
# Output:
#   STRING
def getRetString(ret_val):
  if ret_val >= 0 and ret_val < len(RET_STRING):
    return RET_STRING[ret_val]
  else:
    return "UNDEFINED_RET_VAL"