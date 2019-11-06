"""
PIP is a package manager for Python packages, or modules if you like.

A package contains all the files you need for a module.
Modules are Python code libraries you can include in your project.
pip --version

# Run all these in the command line of python, not in this tool
"""

# Install PIP
# If you do not have PIP installed, you can download and install it from this page: https://pypi.org/project/pip/

# PIP Version check
# C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip --version

# To install a package
# C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip install camelcase

# To UnInstall a package
# C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip uninstall camelcase

# List Packages
# C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip list


print("# Below code will not run since the camelcase is not installed")
import camelcase
c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))


print("# EOF")