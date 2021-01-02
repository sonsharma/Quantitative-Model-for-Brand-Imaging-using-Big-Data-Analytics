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
		z = lambda x: re.compile('\#').sub('', re.compile('RT @[\w_]+:').sub('@', x).strip())
		text_removedRT=z(d['text'])
		text_removedLinks= re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))'''," ",text_removedRT)
		review=re.sub('[!:#`,.\'\"~$@%?/\r\n\t\[\]\(\)\{\}]','', text_removedLinks.encode('ascii','ignore').lower())
		businessid=str(d['business_id'])
		rating=int(d['stars'])
		print '%s,%s,"%s",%s,%d' % (key,datestamp,review,businessid,rating)
		rows=rows+1
	except:
		pass
