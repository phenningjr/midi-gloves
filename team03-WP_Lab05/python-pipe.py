#!/usr/bin/python

import sys
import re

for arg in sys.argv:
	if arg != sys.argv[0]:
		string1 = arg
		if re.search(r"(Hello|Hi|Pogo)", string1):
			print "At least one of Hello, Hi, or Pogo is contained in " + string1
