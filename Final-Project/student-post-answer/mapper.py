#!/usr/bin/python

# input are in the format:
# id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string,
# last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked
#
# output are in the format:
# author_id\thour


import sys
import csv
import re
from datetime import datetime

reader = csv.reader(sys.stdin, delimiter='\t')
reader.next()


for data in reader:
	if len(data) != 19:
		continue
	node_id = data[0]
	body = data[4]
	node_type = data[5]
	parent_id = data[6]
	if node_type == "question" :
		print("{0}\t{1}\t{2}".format(node_id, "A", len(body)))
	elif node_type == "answer":
		print("{0}\t{1}\t{2}".format(parent_id, "B", len(body)))
