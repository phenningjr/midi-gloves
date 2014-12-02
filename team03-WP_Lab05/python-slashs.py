#!/usr/bin/python

import sys
import re

for arg in sys.argv:
	if arg != sys.argv[0]:
		string1 = arg
		if re.search(r"\s.*\s", string1):
			print "There are TWO whitespace characters, which may be separated by other characters, in", string1
