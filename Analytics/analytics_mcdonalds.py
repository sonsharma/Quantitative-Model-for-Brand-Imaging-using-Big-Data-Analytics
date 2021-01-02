#!/usr/bin/env/python 3.6.5

import sys, re
from nltk.corpus import stopwords
from nltk.util import ngrams
businessName = 'mcdonalds'
twograms = dict()
stopword = set(stopwords.words('english'))
for line in sys.stdin:
	d = line.strip(" ").split(':')
	if businessName in d[3].lower() or businessName in d[4].lower():
		s = d[2].lower().replace('"', '')
		tokens = [token for token in s.split(" ") if token != ""]
		val = list(ngrams(tokens, 2))
		for i in val:
			x,y = i
			if x not in stopword and y not in stopword:
				tup = x.replace('\'','') + " " + y.replace('\'','')
				if tup in twograms:
					twograms[tup] += 1
				else:
					twograms[tup] = 1
print("\n".join("{!r}:{!r}".format(k, v) for k, v in twograms.items()))
#print(sorted(twograms.items(), key=lambda x: x[1], reverse=True))