import sys
import os

print( sys.version_info )
print( os.name, os.cpu_count() )

print( sys.maxsize )  # the largest object permissable in memory
print( sys.float_info ) # he largest and smallest floating point value permissable