#!/usr/bin/python

import sys
import re

for arg in sys.argv:
	if arg != sys.argv[0]:
		string1 = arg
		if re.search(r"d\Z", string1):
			print string1, "is a string that ends with 'd'"
