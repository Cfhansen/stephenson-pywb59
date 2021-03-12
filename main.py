###Solution to problem 59 from ben stephenson's "the python workbook".

import re

old = re.compile('^[A-Z]{3}[0-9]{3}$')
new = re.compile('^[0-9]{4}[A-Z]{3}$')

if old.match(mystr_):
  print('This is a valid old-style license plate.')
elif new.match(mystr_):
  print('This is a valid new-style license plate.')
else:
  print('This is not a valid license plate.')
