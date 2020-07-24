#!/usr/bin/python

# input are in the format:
# id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string,
# last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked
#
# output are in the format:
# author_id\thour


import sys
from datetime import datetime
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
reader.next()
for data in reader:
    if len(data) != 19:
         continue

    tagnames = data[2]
    tags = tagnames.strip().split(" ")
    for tag in tags:
    	print("{0}".format(tag))