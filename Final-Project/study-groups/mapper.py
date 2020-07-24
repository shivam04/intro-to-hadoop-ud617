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

    author_id = data[3]
    node_id = data[0]
    parent_id = data[6]
    node_type = data[5]
    if node_type == "question":
    	print("{0}\t{1}".format(node_id, author_id))
    else:
    	print("{0}\t{1}".format(parent_id, author_id))
