#!/usr/bin/env python

"""
Logfind: implementation of http://projectsthehardway.com/2015/06/16/project-1-logfind-2/
"""
import os
import sys
import glob

def main():
    sys.argv.pop(0)
    conffile = os.environ['HOME'] + '/.logfind'
    files = conf_to_files(conffile)

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

main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
