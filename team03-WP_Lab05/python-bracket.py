#!/usr/bin/python

import sys
import re

for arg in sys.argv:
	if arg != sys.argv[0]:
		string1 = arg
		if re.search(r"[aeiou]+", string1):
			print string1 + " contains one or more vowels."
