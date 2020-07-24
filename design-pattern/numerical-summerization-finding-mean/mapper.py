#!/usr/bin/python
import sys
import csv
import re
from datetime import datetime

reader = csv.reader(sys.stdin, delimiter='\t')
reader.next()

for line in reader:
	# parse
    data = line.strip().split('\t')

    if len(data) != 6:
        continue

    date = data[0]
    sale = data[4]
    weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
    print '{0}\t{1}'.format(weekday, sale)
