"""
Build a Python application that can execute a command line and display the
installed version of Python. Use “python -V” to get python version information.
"""

"""
Jupyter Code
python_version = !python -V
print(python_version)
"""
#General Script code
import os
os.system("python -V")