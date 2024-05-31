
# Fix for codespace if failing with CHROMA
# https://github.com/microsoft/autogen/issues/251

# Watchout what sqlite3 version your python interpreter pickups



import pysqlite3 as sqlite3

import os

# Print the version of the sqlite3 library used by Python
print("SQLite version:", sqlite3.sqlite_version)

# Try to determine the location of the sqlite3 library used by Python
# This part is more heuristic and may not always provide accurate results,
# as Python's sqlite3 does not directly expose the library path.
try:
    from ctypes.util import find_library
    sqlite_lib_path = find_library('sqlite3')
    print("SQLite library path:", sqlite_lib_path or "Not found")
except ImportError:
    print("ctypes module is not available, cannot find the library path.")
