#!/usr/bin/env python

"""
Logfind: implementation of http://projectsthehardway.com/2015/06/16/project-1-logfind-2/
"""
import os
import sys
import glob
import mmap

def main():
    if len(sys.argv) < 2:
        usage()
        return
    sys.argv.pop(0)
    conffile = os.environ['HOME'] + '/.logfind'
    files = conf_to_files(conffile)

    if sys.argv[0] == '-o':
        sys.argv.pop(0)
        matched_logs = search(files, sys.argv, 'or')
        for log in matched_logs:
            print log
    else:
        matched_logs = search(files, sys.argv, 'and')
        for log in matched_logs:
            print log

def usage():
    print "logfind: find strings in logfiles\n"
    print "usage:",sys.argv[0],"[-o] string ...\n\n\t -o use OR semantics\n"

# convert regexps in the config file to a list of log files to process
# ignore lines in the config file beginning with '#'
def conf_to_files(conffile):
    conf = open(conffile, 'r')

    regexps = []
    for line in conf:
        if not line.startswith('#'):
            regexps.append(line.rstrip())
    #print regexps

    strings = []
    for arg in sys.argv:
        strings.append(arg)
    #print strings

    files = []

    for regexp in regexps:
        files += glob.glob(regexp)
    #print files

    return files

# takes a list of files, a list of words to search for and a comparison type
# ('and' or 'or') and returns a list of files that contains all of those words
# ('and' mode) or at least one of the words ('or' mode)
def search(files, words, comparison):
    matched_logs = []

    for file in files:
        matched_and = True
        matched_or = False
        f = open(file)
        s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        for word in words:
            matched_and = matched_and and (s.find(word) != -1)
            matched_or = matched_or or (s.find(word) != -1)
        if comparison == 'and' and matched_and:
            matched_logs.append(file)
        elif comparison == 'or' and matched_or:
            matched_logs.append(file)
    return matched_logs

main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
