#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
import sys
import json
import re
reload(sys)
sys.setdefaultencoding('utf-8')

for line in sys.stdin:
	try:
		d = json.loads(line)
		Business_id = str(d['business_id'])
		Business_name=str(d['name']).encode('ascii','ignore')
		print '%s,%s,%s,%s' % (Business_id,Business_name,City,State)
	except:
		pass