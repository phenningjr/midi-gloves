#!/usr/bin/python

import sys
import re

for arg in sys.argv:
	string1 = arg
	if arg != sys.argv[0]:
		if re.search(r"H.?e", string1):
			print "There is an 'H' and a 'e' separated by 0-1 characters (Ex: He Hoe)\n"
