#
# Python DEBUG console printer
#
# Written by Andrew Louie 2019
#

import sys

##################
# DEBUG CONSTANTS: copy to your file or use a number
##################
DBG_CRITICAL = 0
DBG_INFO = 1
DBG_VERBOSE = 2
DBG_ALL = 3


##################
# DEBUG VARIABLES - DO NOT EDIT MANUALLY
##################
# debug level, do not change
DBG_LEVEL = DBG_ALL
# debug file name
DBG_FILE_NAME = "debug.py"
# file name of initializing file
FILE_NAME = "FILE_UNDEFINED"
# state of debug, enabled or disabled
ENABLED = False
# state of debug info
QUIET_MODE = False

##################
# DEBUG FUNCTIONS
##################
# sets level of verobsity to print
# WARNING: If multiple users use dbgSetLevel, the level is bound to change everywhere,
#   recommended to only use this for testing then remove the line in your code
#
# Input:
#   int_level: INT value of minimum level to print DBG_CRITICAL, DBG_INFO, DBG_VERBOSE, DBG_ALL
def setLevel(int_level):
  global DBG_LEVEL, QUIET_MODE
  DBG_LEVEL = int_level
  if not QUIET_MODE:
    print("debug.py (DBG-INFO): " + FILE_NAME + ", debug level set to" + dbgLevelString(int_level))


# enables a file's console prints
#
def enable():
  global ENABLED
  ENABLED = True
  if not QUIET_MODE:
    print("debug.py (DBG-INFO): " + FILE_NAME)


# disables a file's console prints
#
def disable():
  global ENABLED
  ENABLED = False
  if not QUIET_MODE:
    print("debug.py (DBG-INFO): " + FILE_NAME + ", console printing disabled")

# enable debug.py informational prints
#
def quietMode(bool_quiet):
  global QUIET_MODE
  QUIET_MODE = bool_quiet
  if not QUIET_MODE:
    print("debug.py (DBG-INFO): debug.py, info printing enabled")


# init function
# Input:
#   int_level: INT value of level to print, will print everything below as well
#   string_filename: STRING of file name youre initializing debug in
def initFile(int_level, string_filename):
  global FILE_NAME, DBG_LEVEL, ENABLED
  FILE_NAME = str(string_filename)
  DBG_LEVEL = int_level
  ENABLED = True
  if not QUIET_MODE:
    print("debug.py (DBG-INIT): " + FILE_NAME + " init, settings:" + dbgLevelString(DBG_LEVEL) \
    + " (Enabled = " + str(ENABLED) + ")")


def dprintHeader(int_level, int_tabs=0):
  if int_level <= DBG_LEVEL and ENABLED:
    tabs = dbgMakeTabs(int_tabs)
    sys.stdout.write(dbgHeader(tabs, int_level))
    sys.stdout.flush()

# prints without a new line
#
# Input:
#   string_output: STRING to output
#   int_tabs: (OPTIONAL) INT number of tabs to print before output
def dprint(int_level, string_output, int_tabs=0):
  if int_level <= DBG_LEVEL and ENABLED: 
    tabs = dbgMakeTabs(int_tabs)
    sys.stdout.write(tabs + str(string_output))
    sys.stdout.flush()


# prints with a newline
#
# Input:
#   int_level: LEVEL and below to print at
#   string_output: STRING to output
#   int_tabs: (OPTIONAL) INT number of tabs to print before output
def dprintln(int_level, string_output, int_tabs=0):
  if int_level <= DBG_LEVEL and ENABLED:
    tabs = dbgMakeTabs(int_tabs)
    print(dbgHeader(tabs, int_level) + str(string_output))



# prints a list with commas
# useful for printing lists line by line OR a subset of a list
#
# Input:
#   int_level: LEVEL and below to print at
#   list_output: LIST to output
#   int_tabs: (OPTIONAL) INT number of tabs to print before output
#   int_start:  (OPTIONAL) INDEX to start print (if an invalid int_start is sent, will send in list range)
#   int_end:  (OPTIONAL) INDEX to end print (if an invalid int_start is sent, will send in list range)
def dprintList(int_level, list_output, int_tabs=0, int_start=0, int_end=0):
  if int_level <= DBG_LEVEL and ENABLED:
    output = ""
    if int_start == 0 and int_end == 0:
      int_start = 0
      int_end = len(list_output)
    tabs = dbgMakeTabs(int_tabs)
    # iterate and print
    for i in range(0, len(list_output)):
      if i >= int_start and i <= int_end:
        output += str(list_output[i])
        if (i < int_end) and (i < len(list_output) - 1):
          output += ", "
    print(tabs + output)


# prints a list with newlines
# useful for printing lists line by line OR a subset of a list
#
# Input:
#   int_level:
#   list_output: LIST to output
#   int_tabs: (OPTIONAL) INT number of tabs to print before output
#   int_start:  INDEX to start print (if an invalid int_start is sent, will send in list range)
#   int_end:  INDEX to end print (if an invalid int_start is sent, will send in list range)
def dprintListln(int_level, list_output, int_tabs=0, int_start=0, int_end=0):
  if int_level >= DBG_LEVEL and ENABLED:
    if int_start == 0 and int_end == 0:
      int_start = 0
      int_end = len(list_output)
    tabs = dbgMakeTabs(int_tabs)
    # iterate and print
    for i in range(0, len(list_output)):
      if i > int_start and i < int_end:
        print(tabs + "[" + str(i)  + "]: " + str(list_output[i]))
        #sys.stdout.flush()



##################
# PRIVATE FUNCTIONS, do not call
##################
# formatting the print
def dbgLevelString(int_level):
  if int_level < DBG_CRITICAL:
    return " (UNDEFINED"
  elif int_level == DBG_CRITICAL:
    return " (CRITICAL)"
  elif int_level == DBG_INFO:
    return " (INFO)"
  elif int_level == DBG_VERBOSE:
    return " (VERBOSE)"
  elif int_level == DBG_ALL:
    return " (ALL)"
  else:
    return " (DEV-" + str(int_level) + ")"

# format the tabs
def dbgHeader(tabs, int_level):
  return tabs + FILE_NAME + dbgLevelString(int_level) + ": "

# make the tabs
def dbgMakeTabs(int_tabs):
  tabs = ""
  for i in range(int_tabs):
    tabs += "\t"
  return tabs