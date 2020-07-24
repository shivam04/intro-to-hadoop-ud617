#!/usr/bin/python
import sys

count = 0
oldKey = None
for line in sys.stdin:
  data = line.strip().split("\t")
  if len(data) != 1:
  # Something has gone wrong. Skip this line.
    continue

  thisKey = data
  if oldKey and oldKey != thisKey:
    print(oldKey, "\t", count)
    oldKey = thisKey
    count = 0

  oldKey = thisKey
  count += 1

if oldKey != None:
  print(oldKey, "\t", count)