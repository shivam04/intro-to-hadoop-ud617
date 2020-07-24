#!/usr/bin/python

import sys

def compare(a , b):
    if a[1] > b[1]:
        return -1
    elif a[1] < b[1]:
        return 1
    return 0

last_tag = None
count = 0
ans = []
for line in sys.stdin:
    tag = line.strip()
    if last_tag and last_tag != tag:
        ans.append((last_tag, count))
        count = 0
        last_tag = tag

    last_tag = tag
    count += 1

if last_tag:
    ans.append((last_tag, count))

ans = sorted(ans, cmp=compare)

print("Tag\tCount")

for i in range(0, 10):
    print("{0}\t{1}".format(ans[i][0], ans[i][1]))