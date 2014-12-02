#!/usr/bin/python

import sys
import re

for arg in sys.argv:
	if arg != sys.argv[0]:
		string1 = arg
		if re.search(r"\D", string1):
			print "There is at least one character in", string1, "that is not a digit."
