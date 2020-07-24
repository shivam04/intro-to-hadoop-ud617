#!/usr/bin/python

import sys

qlength = 0
alength = 0
acount = 0
last_qid = None

print("{0}\t|{1}\t|{2}".format("Question Node ID", "Question Length", "Average Answer Length"))

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) != 3:
        continue

    qid, node_type, body_length =  data

    body_length = int(body_length)

    if last_qid and last_qid != qid:
        avg = 0
        try:
            avg = float(alength)/float(acount)
        except:
            avg = 0
        print("{0}\t{1}\t{2}".format(last_qid, qlength, avg))
        last_qid = qid
        qlength = 0
        alength = 0
        acount = 0

    last_qid = qid
    if node_type == "A":
        qlength += body_length
    elif node_type == "B":
        alength += body_length
        acount += 1

if last_qid:
    avg = 0
    try:
        avg = float(alength)/float(acount)
    except:
        avg = 0
    print("{0}\t{1}\t{2}".format(qid, qlength, avg))