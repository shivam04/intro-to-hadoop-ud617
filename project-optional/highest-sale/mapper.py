#!/usr/bin/python
import sys

def mapper():
    # read standard input line by line
    for line in sys.stdin:
        # strip off extra whitespace, split on tab and put the data in an array
        data = line.strip().split("\t")

        # This is the place you need to do some defensive programming
        # what if there are not exactly 6 fields in that line?
        # YOUR CODE HERE
        if len(data) != 6:
            continue
            
        date, time, store, item, cost, payment = data
        
        # Now print out the data that will be passed to the reducer
        print("{0}\t{1}".format(store, cost))

# This function allows you to test the mapper with the provided test string
def main():
    import StringIO
    mapper()
    sys.stdin = sys.__stdin__

main()