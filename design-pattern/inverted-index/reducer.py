#!/usr/bin/python

import sys
import collections

# only print 'fantastic' and 'fantastically'
inverted_index = collections.defaultdict(list)

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue
    word = data[0]
    node_id = data[1]
    inverted_index[word].append(node_id)

for word in inverted_index:
    if word == 'fantastic' or word == 'fantastically':
    	inverted_index[word].sort()
        print "{0}\t{1}\t{2}".format(word, len(inverted_index[word]), inverted_index[word])