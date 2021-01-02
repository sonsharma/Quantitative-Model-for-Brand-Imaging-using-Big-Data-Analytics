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
        review=d[1]
        print '%s : %s : "%s" : Starbucks :  :  :  :  ' % (key,date_new,review)