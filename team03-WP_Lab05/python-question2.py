#!/usr/bin/python

import sys
import re

for arg in sys.argv:
	if arg != sys.argv[0]:
		string1 = arg
		if re.search(r"l.+?o", string1):
			print "The non-greedy match with 'l' followed by\n one or more characters is 'llo' rather than\n 'llo wo'."
