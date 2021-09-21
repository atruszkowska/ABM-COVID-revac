import subprocess

import sys
py_path = '../../scripts/'
sys.path.insert(0, py_path)

import utils as ut
from colors import *

py_version = 'python3'

#
# Compile and run all the places class(es) specific tests
#

# Compile
subprocess.call([py_version + ' compilation.py'], shell=True)

# Test suite 1
ut.msg('Place-derived classes functionality tests', CYAN)
subprocess.call(['./places_test'], shell=True)


