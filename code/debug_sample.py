from debug import debug as dbg

# These values can be used as integers, they wont change in value
# if you specify an integer HIGHER than 3 then everything will show
CRITICAL = 0
INFO = 1
VERBOSE = 2
ALL = 3

# This functionc all is required to set a filename and verbosity level
# if not called, the dprint statements will output everything
dbg.initFile(CRITICAL, "debug_sample.py")

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




#################################
# Extra calls to customize your DEBUG printing
#################################
dbg.dprint(CRITICAL, "\n\n\n")
dbg.dprint(CRITICAL, "=== Examples of controlling debug.py ===\n")

# setting a verbosity level, this is done in initFile, 
# but it's an option if you want it
dbg.setLevel(INFO)

# enable and disable all printing from your file
dbg.disable()
dbg.dprint(INFO, "DISABLED - This text wont show")
dbg.enable()
dbg.dprintln(INFO, "ENABLED - This text will show\n")

# Quiet mode is for when you dont want debug.py from displaying any
# informational sets, disables, and enables
dbg.quietMode(True)
# informational text from these wont show
dbg.disable()
dbg.enable()
dbg.setLevel(INFO)
dbg.initFile(VERBOSE, "debug_sample.py")

# you have extra debug levels if you want
dbg.quietMode(False)
dbg.setLevel(5)
dbg.dprintln(5, "This was printed with a user defined print level")