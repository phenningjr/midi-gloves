#!/usr/bin/python

import sys
import re

for arg in sys.argv:
	if arg != sys.argv[0]:
		string1 = arg
		if re.search(r"\W", string1):
			print "The space between Hello and World is not alphanumeric"
