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
    conf = open(conffile, 'r')

    regexps = []
    for line in conf:
        regexps.append(line.rstrip())
    #print regexps

    strings = []
    for arg in sys.argv:
        strings.append(arg)
    #print strings

    files = regexps_to_files(regexps[:])

# convert regexps in the config file to a list of log files to process
def regexps_to_files(regexps):
    files = []

    for regexp in regexps:
        files += glob.glob(regexp)

    print files

main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
