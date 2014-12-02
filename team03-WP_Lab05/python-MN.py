#!/usr/bin/python

import sys
import re

for arg in sys.argv:
	if arg != sys.argv[0]:
		string1 = arg
		if re.search(r"l{1,2}", string1):
			print "There exists a substring with at least 1\n" + "and at most 2 1's in " + string1
