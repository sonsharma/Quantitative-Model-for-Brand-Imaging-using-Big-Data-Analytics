#!/usr/bin/python 2.6.6 
# -*- coding: utf-8 -*-

import re
import time
import csv
from csv import reader
import sys
reload(sys)
from datetime import datetime
sys.setdefaultencoding('utf-8')


for line in reader(sys.stdin) :
        d=line
        key = d[0]
        try:
                d[2]=d[2].rstrip('\n')
	        date = datetime.strptime(d[2],"%Y-%m-%d %H:%M:%S")
		date_new = date.strftime('%d-%m-%Y')
                #datestamp=time.strftime('%m-%d-%Y',time.strptime(d[2],'%Y-%m-%d %H:%M'))
        except:
                date_new=''
        z = lambda x: re.compile('\#').sub('', re.compile('RT @[\w_]+:').sub('@', x).strip())
        text_removedRT=z(d[1])
        text_removedLinks= re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))'''," ",text_removedRT)
        review=re.sub('[!#:`,.\'\"~*$@%?/\r\t\n\[\]\(\)\{\}]','', text_removedLinks.encode('ascii','ignore').lower())
        print '%s : %s : "%s" : Starbucks :  :  :  :  ' % (key,date_new,review)