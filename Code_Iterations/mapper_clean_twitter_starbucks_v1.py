#!/usr/bin/env python2.6.6
# -*- coding: utf-8 -*-
import re
import sys
import json
import time

for line in sys.stdin:
        try:
                d=json.loads(line)
                key=str(d['id_str'])
                datestamp=time.strftime('%m-%d-%Y',time.strptime(d['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))
                z = lambda x: re.compile('\#').sub('', re.compile('RT @[\w_]+:').sub('@', x).strip())
                review=d[1]
                business_name = str(d['user']['name'])
                print '%s : %s : "%s" : Starbucks :  :  :  : ' % (key,datestamp,review)
        except:
                pass