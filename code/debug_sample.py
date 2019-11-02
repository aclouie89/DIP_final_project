import sys

from debug import debug as dbg
# These values can be used as integers, they wont change in value
# if you specify an integer HIGHER than 3 then everything will show
# CRITICAL = 0
# INFO = 2
# VERBOSE = 3
# ALL = 4
CRITICAL = dbg.CRITICAL
INFO = dbg.INFO
VERBOSE = dbg.VERBOSE
ALL = dbg.ALL

#
# Printing with control over output
#
dbg.dprintln(INFO, "INFO is too high, this wont print")
dbg.dprintln(VERBOSE, "Verbose is too high, this wont print")
dbg.dprintln(ALL, "ALL is too high this wont print")

#
# Printing without a newline
# has optional 3rd argument for tabs
#
dbg.dprintHeader(CRITICAL)
dbg.dprint(CRITICAL, "Text without")
dbg.dprint(CRITICAL, " a newline")
dbg.dprint(CRITICAL, "and one tab ", 1)
dbg.dprint(CRITICAL, "in the middle\n")


#
# Printing with a newline
# has optional 3rd argument for tabs
#
dbg.dprintln(CRITICAL, "Text with a new line")
dbg.dprintln(CRITICAL, "Text with a new line and one tab", 1)
dbg.dprintln(CRITICAL, "Text with a new line and two tabs", 2)


#
# Printing from a function
#
def Function():
  dbg.dprintln(CRITICAL, "Text from a function")
Function()


#
# Printing lists - For ease of use
# all list printing functions have 3 optional parameters
# (INT) tabs, (INT) start_index, (INT) end_index
#
test_list = [0,1,2,3,4]
dbg.dprintln(CRITICAL, "Printing a list with dprintln: ")
dbg.dprintln(CRITICAL, test_list)

dbg.dprintln(CRITICAL, "Printing a list with commas tabbed over once: ")
dbg.dprintList(CRITICAL, test_list, 1)

dbg.dprintln(CRITICAL, "Printing a list with newlines: ")
dbg.dprintListln(CRITICAL, test_list)

dbg.dprintln(CRITICAL, "Printing a list between index [1] and [2]")
dbg.dprintList(CRITICAL, test_list, 0, 1, 2)