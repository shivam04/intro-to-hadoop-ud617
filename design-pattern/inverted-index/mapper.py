#!/usr/bin/python
import sys
import csv
import re
from datetime import datetime

reader = csv.reader(sys.stdin, delimiter='\t')
reader.next()

for line in reader:
	# parse
    node_id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id,\
    added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at,\
    active_revision_id,	extra, extra_ref_id, extra_count, marked = line

    hour = datetime.strptime(added_at.split(".")[0], "%Y-%m-%d %H:%M:%S").hour

    # for debug:
    '''
    print "\nNew entry -------------------------------------------------\n\n"
    print "id\t{0}".format(node_id)
    print "title\t{0}".format(title)
    print "tagnames\t{0}".format(tagnames)
    print "author_id\t{0}".format(author_id)
    print "body\t{0}".format(body)
    print "node_type\t{0}".format(node_type)
    print "parent_id\t{0}".format(parent_id)
    print "abs_parent_id\t{0}".format(abs_parent_id)
    print "added_at\t{0}".format(added_at)
    print "hour\t{0}".format(hour)
    '''
    node_id = line[0]
    body = line[4]
    body_words = re.findall(r"[a-zA-Z]+", body)  #  '[a-zA-Z]+' means "a word character (a-z A-Z etc.) repeated one or more times"
    body_words = [word.lower() for word in body_words]
    for word in body_words:
    	print "{0}\t{1}".format(word, node_id)