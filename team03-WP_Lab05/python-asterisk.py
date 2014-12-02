#!/usr/bin/python

import sys
import re

for arg in sys.argv:
	if arg != sys.argv[0]:
		string1 = arg
		if re.search(r"el*o", string1):
			print "There is an 'e' followed by zero to many\n'l' followed by 'o' (eo, elo, ello, elllo)."
