#!/usr/bin/python

import sys

last_day = None
total_sales = 0
day_count = 0

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) != 2:
        continue
    this_day = data[0]
    sale = data[1]

    if last_day and last_day != this_day:
        average_sale = float(total_sales) / float(day_count)
        print(last_day, '\t', average_sale)
        last_day = this_day
        total_sales = 0
        day_count = 0

    last_day = this_day
    total_sales += float(sale)
    day_count += 1

if last_day is not None:
    average_sale = float(total_sales) / float(day_count)
    print(last_day, '\t', average_sale)