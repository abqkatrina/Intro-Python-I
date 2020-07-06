"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line -- ???

print(sys.argv)
['']

# Print out the OS platform you're using:

print(sys.platform)
'win32'

# Print out the version of Python you're using:

print(sys.version)
'3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)]'


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID -- what does this number mean?
print(os.getpid())
104

# Print the current working directory (cwd):
print(os.getcwd())
C:\...\Programs\Python\Python38-32


# Print out your machine's login name -- is this the current user name?
print(os.getlogin())
ini42