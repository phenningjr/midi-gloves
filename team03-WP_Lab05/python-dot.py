#! /usr/bin/python

import sys
import re

for x in sys.argv:
	print x
	string1 = x
	if re.search(r".....", string1):
		print string1 + " has length >= 5"


