#!/usr/bin/env python

import sys
profile_id=[0]*9
profile_date=[0]*5
profile_review=[0]*5
profile_id[0]='String'
profile_date[0]='String'
profile_review[0]='String'
profile_id[3]='No'
profile_date[3]='No'
profile_review[3]='No'
rows=0
for line in sys.stdin:
        line  = line.split(":")
        if len(line[0])=='':
                profile_id[3]='Yes'
        elif len(line[0])>profile_id[1]:
                profile_id[1]=len(line[0])
        if len(line[1])=='':
                profile_date[3]='Yes'
        elif len(line[1])>profile_date[1]:
                profile_date[1]=len(line[1])
        if len(line[2])=='':
                profile_profile[3]='Yes'
        elif len(line[2])>profile_review[1]:
                profile_review[1]=len(line[2])

        if sys.getsizeof(line[0])>profile_id[2]:
                profile_id[2]=sys.getsizeof(line[0])
        if sys.getsizeof(line[1])>profile_date[2]:
                profile_date[2]=sys.getsizeof(line[1])
        if sys.getsizeof(line[2])>profile_review[2]:
                profile_review[2]=sys.getsizeof(line[2])
        rows=rows+1
print '\nTotal rows of Review Data: %s' % (rows)
print 'Column Profiles for Twitter Data:'
print '1) ID'
print '   Data Type: %s\n   Max String Length: %s\n   Max String Size(bytes): %s\n   Range: Doesn\'t Apply\n   Contains Null: %s\n   is_primary_key: Yes' % (profile_id[0],profile_id[1],profile_id[2],profile_id[3])
print '2) Date'
print '   Data Type: %s\n   Max String Length: %s\n   Max String Size(bytes): %s\n   Range: Doesn\'t Apply\n   Contains Null: %s\n   is_primary_key: No' % (profile_date[0],profile_date[1],profile_date[2],profile_date[3])
print '3) Review'
print '   Data Type: %s\n   Max String Length: %s\n   Max String Size(bytes): %s\n   Range: Doesn\'t Apply\n   Contains Null: %s\n   is_primary_key: No' % (profile_review[0],profile_review[1],profile_review[2],profile_review[3])
print