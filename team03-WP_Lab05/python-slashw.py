#!/usr/bin/python

import sys
import re

for arg in sys.argv:
	if arg != sys.argv[0]:
		string1 = arg
		m_obj = re.search(r"(\w\w)", string1)
		if m_obj:
			print "The first two adjacent alphanumeric characters (A-z, a-z, 0-9, _) in", string1, "were", m_obj.group(1)


