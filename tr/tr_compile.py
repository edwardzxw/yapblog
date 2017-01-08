#!flask/bin/python
import os
import sys
'''
if sys.platform == 'win32':
    pybabel = 'flask\\Scripts\\pybabel'
else:
    pybabel = 'flask/bin/pybabel'
'''
pybabel = 'pybabel'
app = '..'
os.system(pybabel + ' compile -d {0}/translations'.format(app))
