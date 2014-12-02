#!/usr/bin/python

import sys
import re

for arg in sys.argv:
	if arg != sys.argv[0]:
		string1 = arg
		if re.search(r"llo\b", string1):
			print "There is a word that ends with 'llo'"
		else:
			print "There are no words that end with 'llo'"
