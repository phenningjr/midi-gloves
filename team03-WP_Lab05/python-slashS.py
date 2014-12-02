#!/usr/bin/python

import sys
import re

for arg in sys.argv:
	if arg != sys.argv[0]:
		string1 = arg
		m_obj = re.search(r"(\S*)\s*(\S*)", string1)
		if m_obj:
			print "The first two groups of NON-whitespace characters are '%s' and '%s'." % m_obj.groups()
