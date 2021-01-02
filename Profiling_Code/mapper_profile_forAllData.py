#!/usr/bin/env python

import sys
profile_id=[0]*9
profile_date=[0]*5
profile_review=[0]*5
profile_businessid=[0]*5
profile_businessname=[0]*5
profile_stars=[0]*5
profile_state=[0]*5
profile_city=[0]*5

profile_id[0]='String'
profile_date[0]='String'
profile_review[0]='String'
profile_id[3]='No'
profile_date[3]='No'
profile_review[3]='No'

profile_businessid[0]='String'
profile_businessid[3]='yes'
profile_businessname[0]='String'
profile_businessname[3]='yes'
profile_stars[0]='Int'
profile_stars[3]='yes'
profile_state[0]='String'
profile_state[3]='yes'
profile_city[0]='String'
profile_city[3]='yes'
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

        if len(line[3])>profile_businessid[1]:
                profile_businessid[1]=len(line[3])
        if len(line[4])>profile_businessname[1]:
                profile_businessname[1]=len(line[4])
        if len(line[5])>profile_stars[1]:
                profile_stars[1]=len(line[5])
        if len(line[6])>profile_city[1]:
                profile_city[1]=len(line[6])
        if len(line[7])>profile_state[1]:
                profile_state[1]=len(line[7])


        if sys.getsizeof(line[0])>profile_id[2]:
                profile_id[2]=sys.getsizeof(line[0])
        if sys.getsizeof(line[1])>profile_date[2]:
                profile_date[2]=sys.getsizeof(line[1])
        if sys.getsizeof(line[2])>profile_review[2]:
                profile_review[2]=sys.getsizeof(line[2])
        if sys.getsizeof(line[3])>profile_businessid[2]:
                profile_businessid[2]=sys.getsizeof(line[3])
        if sys.getsizeof(line[4])>profile_businessname[2]:
                profile_businessname[2]=sys.getsizeof(line[4])
        if sys.getsizeof(line[5])>profile_stars[2]:
                profile_stars[2]=sys.getsizeof(line[5])
        if sys.getsizeof(line[6])>profile_city[2]:
                profile_city[2]=sys.getsizeof(line[6])
        if sys.getsizeof(line[7])>profile_state[2]:
                profile_state[2]=sys.getsizeof(line[7])      

        rows=rows+1
print '\nTotal rows of Review Data: %s' % (rows)
print 'Column Profiles for Twitter Data:'
print '1) ID'
print '   Data Type: %s\n   Max String Length: %s\n   Max String Size(bytes): %s\n   Range: Doesn\'t Apply\n   Contains Null: %s\n   is_primary_key: Yes' % (profile_id[0],profile_id[1],profile_id[2],profile_id[3])
print '2) Date'
print '   Data Type: %s\n   Max String Length: %s\n   Max String Size(bytes): %s\n   Range: Doesn\'t Apply\n   Contains Null: %s\n   is_primary_key: No' % (profile_date[0],profile_date[1],profile_date[2],profile_date[3])
print '3) Review'
print '   Data Type: %s\n   Max String Length: %s\n   Max String Size(bytes): %s\n   Range: Doesn\'t Apply\n   Contains Null: %s\n   is_primary_key: No' % (profile_review[0],profile_review[1],profile_review[2],profile_review[3])
print '4) Business ID'
print '   Data Type: %s\n   Max String Length: %s\n   Max String Size(bytes): %s\n   Range: Doesn\'t Apply\n   Contains Null: %s\n   is_primary_key: No' % (profile_businessid[0],profile_businessid[1],profile_businessid[2],profile_businessid[3])
print '5) Business Name'
print '   Data Type: %s\n   Max String Length: %s\n   Max String Size(bytes): %s\n   Range: Doesn\'t Apply\n   Contains Null: %s\n   is_primary_key: No' % (profile_businessname[0],profile_businessname[1],profile_businessname[2],profile_businessname[3])
print '6) User Rating'
print '   Data Type: %s\n   Max String Length: %s\n   Max String Size(bytes): %s\n   Range: Doesn\'t Apply\n   Contains Null: %s\n   is_primary_key: No' % (profile_stars[0],profile_stars[1],profile_stars[2],profile_stars[3])
print '7) City'
print '   Data Type: %s\n   Max String Length: %s\n   Max String Size(bytes): %s\n   Range: Doesn\'t Apply\n   Contains Null: %s\n   is_primary_key: No' % (profile_city[0],profile_city[1],profile_city[2],profile_city[3])
print '8) State'
print '   Data Type: %s\n   Max String Length: %s\n   Max String Size(bytes): %s\n   Range: Doesn\'t Apply\n   Contains Null: %s\n   is_primary_key: No' % (profile_state[0],profile_state[1],profile_state[2],profile_state[3])

