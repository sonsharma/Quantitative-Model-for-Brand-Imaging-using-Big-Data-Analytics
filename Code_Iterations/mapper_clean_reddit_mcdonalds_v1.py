#!/usr/bin/python 2.6.6 
# -*- coding: utf-8 -*-

import re
import time
import csv
from csv import reader
import sys
from datetime import datetime
reload(sys)
sys.setdefaultencoding('utf-8')

for line in reader(sys.stdin) :
	d=line
        key = d[0]
        try:
                d[2]=d[2].rstrip('\n')
                datestamp=time.strftime('%m-%d-%Y',time.strptime(d[2],'%m/%d/%Y %H:%M'))
        except:
		if len(d[2])!= 0:
			continue
        	datestamp=''
        review=d[1]
        print '%s : %s : "%s" : Starbucks :  :  :  :  ' % (key,datestamp,review)