#!/usr/bin/env python
import os, sys

#argument 1 is string
#argument 2 is number
#argument 3 is file
#Used standard search and replace if the name is found

def ch_grade(sys):
	error = "Error: Not enough arguments"
	if len(sys.argv) < 3:
	    output.write(error)
	else:
	    string = sys.argv[1]
	    number = sys.argv[2]
	    input = sys.stdin
	    output = sys.stdout
	    if len(sys.argv) > 3:
		input = open(sys.argv[3])
	    if len(sys.argv) > 4:
		output = open(sys.argv[4], 'w')
	    for s in input.xreadlines():
		output.write(s.replace(string, number))
	return (string, number)

if __name__=='__main__':
    from sys import stdin,stdout,stderr
    #string = sys.argv[1]
    #number = sys.argv[2]
    (string,number) = ch_grade(sys)
    stderr.write(number)
    stderr.write(string)
