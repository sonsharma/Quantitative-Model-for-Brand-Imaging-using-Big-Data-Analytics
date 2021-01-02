#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import csv
import re
import datetime
import time
import csv
from csv import reader
#from importlib import reload
reload(sys)
sys.setdefaultencoding('utf-8')

for line in reader(sys.stdin):
        d=line
        key = d[0]
        try:
                d[2]=d[2].rstrip('\n')
                datestamp=time.strftime('%m-%d-%Y',time.strptime(d[2],'%m/%d/%Y %H:%M'))
        except:
                datestamp=''
        z = lambda x: re.compile('\#').sub('', re.compile('RT @[\w_]+:').sub('@', x).strip())
        review=d[1]
	print '%s : %s : "%s" : McDonalds :  :  :  : ' % (key,datestamp,review)