import sys
import glob
import mmap
import re

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

# takes a list of files, a list of words to search for, a comparison type
# ('and' or 'or'), and regexp_type which specifies whether the words are normal
# or regular expressions and returns a list of files that contains all of those
# words ('and' mode) or at least one of the words ('or' mode)
def search(files, words, or_mode, regexp_mode):
    matched_logs = []

    for file in files:
        matched_and = True
        matched_or = False
        with open(file) as f:
            mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            for word in words:
                if regexp_mode:
                    matched = re.search(word, mm, re.MULTILINE)
                else:
                    matched = (mm.find(word) != -1)
                matched_and = matched_and and matched
                matched_or = matched_or or matched
            if (not or_mode) and matched_and:
                matched_logs.append(file)
            elif or_mode and matched_or:
                matched_logs.append(file)
            mm.close()

    return matched_logs


# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
