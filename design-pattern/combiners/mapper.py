#!/usr/bin/python
import sys
from datetime import datetime

for line in sys.stdin:
	# parse
    data = line.split('\t')

    if len(data) != 6:
        continue

    date = data[0]
    sale = data[4]
    weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
    print '{0}\t{1}'.format(weekday, sale)