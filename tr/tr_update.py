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
os.system(pybabel + ' extract -F babel.cfg -k lazy_gettext -o messages.pot {0}'.format(app))
os.system(pybabel + ' update -i messages.pot -d {0}/translations'.format(app))
os.unlink('messages.pot')