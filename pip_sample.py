# go to python script directory: C:\Users\User1\AppData\Local\Programs\Python\Python37\Scripts
# Instead of going to the directory above we can run pip by python -m pip
# run pip install camelcase (if not in the directory python -m pip install camelcase)
# to list installed packages run pip list
# to uninstall a package run pip uninstall packagename
# For pycharm just go to the package name,
# press Alt+Enter and import package (this will install to the virtual environment set for the project in Pycharm)

import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print c.hump(txt)
