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
    time = data[8].split("+")[0]
    hour = datetime.strptime(time, "%Y-%m-%d %H:%M:%S.%f").hour
    print("{0}\t{1}".format(author_id, hour))