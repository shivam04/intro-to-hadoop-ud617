#!/usr/bin/python
import sys

count = 0
oldKey = None
maxPath = None
maxCount = 0
for line in sys.stdin:
  data = line.strip().split("\t")
  if len(data) != 1:
  # Something has gone wrong. Skip this line.
    continue

  thisKey = data
  if oldKey and oldKey != thisKey:
    if count > maxCount:
      maxCount = count
      maxPath = oldKey
    oldKey = thisKey
    count = 0

  oldKey = thisKey
  count += 1

if oldKey != None:
  if count > maxCount:
      maxCount = count
      maxPath = oldKey

print(maxPath, "\t", maxCount)