#!/usr/bin/env python2.6.6
# -*- coding: utf-8 -*- 
import re
import sys
import json
import time
reload(sys)
sys.setdefaultencoding('utf-8')
rows=0
err=0
for line in sys.stdin:
	try:
		d=json.loads(line)
		key=str(d['review_id'])
		datestamp=time.strftime('%m-%d-%Y',time.strptime(d['date'],'%Y-%m-%d %H:%M:%S'))
		review=d[1]
		businessid=str(d['business_id'])
		rating=int(d['stars'])
		print '%s,%s,"%s",%s,%d' % (key,datestamp,review,businessid,rating)
		rows=rows+1
	except:
		pass
