#!/usr/bin/env python2.6.6
# -*- coding: utf-8 -*- 
import re
import sys
import json
import time
reload(sys)
sys.setdefaultencoding('utf-8')
for line in sys.stdin:
	try:
		d=json.loads(line)
		key=str(d['review_id'])
		datestamp=time.strftime('%m-%d-%Y',time.strptime(d['date'],'%Y-%m-%d %H:%M:%S'))
		z = lambda x: re.compile('\#').sub('', re.compile('RT @[\w_]+:').sub('@', x).strip())
		text_removedRT=z(d['text'])
		text_removedLinks= re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))'''," ",text_removedRT)
		review=re.sub('[!:#`,.\'\"~$@%?/\r\n\t\[\]\(\)\{\}]','', text_removedLinks.encode('ascii','ignore').lower())
		print '%s,%s,"%s"' % (key,datestamp,review)
	except:
		pass