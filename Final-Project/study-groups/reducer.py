#!/usr/bin/python

import sys

last_id = None
author_ids = []

print("{0}\t|\t{1}".format("Question Node ID","Student IDs"))

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) != 2:
        continue
    node_id, author_id = data
    if last_id and last_id != node_id:
    	print("{0}\t{1}".format(last_id, author_ids))
        author_ids = []

    last_id = node_id
    author_ids.append(author_id)

if last_id != None:
    print("{0}\t{1}".format(last_id, author_ids))
	