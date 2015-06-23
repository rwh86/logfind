import sys
import glob
import mmap
import re

# convert regexps in the config file to a list of log files to process
# ignore lines in the config file beginning with '#'
def conf_to_files(conffile):
    """Convert filename globs in the conffile (one per line) to a list of log files to process. Ignore lines in the config file beginning with '#'."""
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

def search(files, words, or_mode=False, regexp_mode=False):
    """ Search files for words or regexps using 'and' or 'or' semantics.

    Keyword arguments:
    files -- list of files to search
    words -- list of words (or regexps) to search for
    or_mode -- search for all words when False (AND) (default) or at least one when True (OR)
    regexp_mode -- when True, the words are treated as regexps (default is False)

    Returns a list of files that match
    """
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
