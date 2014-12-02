#!/usr/bin/python

import sys
import re

for arg in sys.argv:
	if arg != sys.argv[0]:
		string1 = arg
		m_obj = re.search(r"(\d+)", string1)
		if m_obj:
			print m_obj.group(1), "is the first number in '" + string1 + "'"
