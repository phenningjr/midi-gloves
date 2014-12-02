
#! /usr/bin/python

import sys
import re

for arg in sys.argv:
	if arg != sys.argv[0]:
		string1 = arg
		m_obj = re.search(r"(H..).(o..)", string1)
		if m_obj:
			print "We matched '" + m_obj.group(1) + "' and '" + m_obj.group(2) + "'"
