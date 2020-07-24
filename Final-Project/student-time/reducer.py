#!/usr/bin/python

import sys

last_id = None
hours_count = dict()
peak_hour = []
max_hour = 0

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) != 2:
        continue
    this_id, this_hour = data
    if last_id and last_id != this_id:
    	for hour in hours_count[last_id]:
    		if hours_count[last_id][hour] == max_hour:
    			peak_hour.append(hour)
    	for h in peak_hour:
            print("{0}\t{1}".format(last_id, h))
        last_id = this_id
        hours_count[last_id] = dict()
        hours_count[last_id][this_hour] = 0
        max_hour = 0
        peak_hour = []

    if last_id == None:
    	last_id = this_id
    	hours_count[last_id] = dict()
    	hours_count[last_id][this_hour] = 0
    if this_hour not in hours_count[last_id]:
    	hours_count[last_id][this_hour] = 0
    hours_count[last_id][this_hour] += 1
    max_hour = max(max_hour, hours_count[last_id][this_hour])




if last_id != None:
	for hour in hours_count[last_id]:
		if hours_count[last_id][hour] == max_hour:
			peak_hour.append(hour)
	for h in peak_hour:
		print("{0}\t{1}".format(last_id, h))