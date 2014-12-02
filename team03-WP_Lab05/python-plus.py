
#! /usr/bin/python

import sys
import re

for arg in sys.argv:
	if arg != sys.argv[0]:
		string1 = arg
		if re.search(r"l+", string1):
			print 'There are one or more consecutive letter "l"' + "'s in " + string1
