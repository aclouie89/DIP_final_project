#
# Python DEBUG console printer
#
# Written by Andrew Louie 2019
#

import sys

##################
# DEBUG CONSTANTS
##################
# Debug levels
CRITICAL = 0
INFO = 1
VERBOSE = 2
ALL = 3
# debug file name
DBG_NAME = "debug.py"


##################
# DEBUG LEVEL
# Change this for your testing needs
##################
DBG_LEVEL = INFO

##################
# DEBUG VARIABLES - DO NOT EDIT MANUALLY
##################
# state of debug, enabled or disabled
ENABLED = True
# state of debug info
QUIET_MODE = False

##################
# DEBUG FUNCTIONS
##################
def dprintHeader(int_level, int_tabs=0):
  if validLevel(int_level):
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
  if validLevel(int_level):
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
  if validLevel(int_level):
    if isinstance(int_level, int):
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
  if validLevel(int_level):
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
  if validLevel(int_level):
    if int_level >= DBG_LEVEL and ENABLED:
      if int_start == 0 and int_end == 0:
        int_start = 0
        int_end = len(list_output)
      tabs = dbgMakeTabs(int_tabs)
      # iterate and print
      for i in range(0, len(list_output)):
        if i > int_start and i < int_end:
          print(tabs + "[" + str(i)  + "]: " + str(list_output[i]))



##################
# PRIVATE FUNCTIONS
# DO NOT CALL THESE
##################
# formatting the print
def dbgLevelString(int_level):
  if int_level < CRITICAL:
    return "<UNDEFINED>"
  elif int_level == CRITICAL:
    return "<CRITICAL>"
  elif int_level == INFO:
    return "<INFO>"
  elif int_level == VERBOSE:
    return "<VERBOSE>"
  elif int_level == ALL:
    return "<ALL>"
  else:
    return "<DEV-" + str(int_level) + ">"

# format the tabs
def dbgHeader(tabs, int_level):
  if QUIET_MODE == False:
    return tabs + dbgLevelString(int_level) + " "
  else:
    return tabs

# make the tabs
def dbgMakeTabs(int_tabs):
  tabs = ""
  for i in range(int_tabs):
    tabs += "\t"
  return tabs

# dumps debug info
def dumpDebugInfo():
  print("\n\ndebug.py(): DEBUG STATE")
  print("\tENABLED: " + str(ENABLED))
  print("\tDBG_LEVEL: " + str(DBG_LEVEL))
  print("\tQUIET_MODE: " + str(QUIET_MODE) + "\n\n")

# sets level of verobsity to print
# WARNING: If multiple users use dbgSetLevel, the level is bound to change everywhere,
#   recommended to only use this for testing then remove the line in your code
#
# Input:
#   int_level: INT value of minimum level to print CRTICIAL, INFO, VERBOSE, ALL
def setLevel(int_level):
  global DBG_LEVEL, QUIET_MODE
  DBG_LEVEL = int_level
  if not QUIET_MODE:
    print("debug.py (DBG-INFO): " + "debug level set to" + dbgLevelString(int_level) + " please only call this once")


# enables a file's console prints
#
def enable():
  global ENABLED
  ENABLED = True
  if not QUIET_MODE:
    print("debug.py (DBG-INFO): console printing enabled")


# disables a file's console prints
#
def disable():
  global ENABLED
  ENABLED = False
  if not QUIET_MODE:
    print("debug.py (DBG-INFO): console printing disabled")

# enable debug.py informational prints
#
def quietMode(bool_quiet):
  global QUIET_MODE
  QUIET_MODE = bool_quiet
  if not QUIET_MODE:
    print("debug.py (DBG-INFO): debug.py, info and tag printing enabled")

# checks if level is an integer
#
def validLevel(int_level):
  if isinstance(int_level, int):
    return True
  else:
    print("debug.py " + str(int_level) + " is not an integer level")
    return False