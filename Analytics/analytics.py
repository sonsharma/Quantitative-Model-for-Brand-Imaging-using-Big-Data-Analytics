#!/user/bin/env python 3.6.5

import sys
import textblob
from textblob import TextBlob

try:
        for line in sys.stdin:
                lines = line.strip().split(':')
                blob = TextBlob(lines[2])
                print(lines[0],':',lines[1],':',lines[3],':',lines[4],':',lines[5],':',lines[6],':',lines[7],':',blob.sentiment[0],':',blob.sentiment[1])
except:
        pass