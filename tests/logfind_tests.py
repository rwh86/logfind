from nose.tools import *
from lf.utils import *
import os

#def setup():
#    print "SETUP!"
#
#def teardown():
#    print "TEAR DOWN!"
#
#def test_basic():
#    print "I RAN!"


class TestClass:
    files = ["./tests/logs1/test1", "./tests/logs1/test2", "./tests/logs2/test3", "./tests/logs2/test4"]

    def setUp(self):
        content = "# this is a test configuration file\n./tests/logs1/test1\n./tests/logs1/test2\n./tests/logs2/test3\n./tests/logs2/test4"
        with open('logfind.config.txt','w') as f:
            f.write(content)

    def tearDown(self):
        os.remove('logfind.config.txt')
      
    def test_conf_to_files(self):
        files = conf_to_files('logfind.config.txt')
        assert files[0] == "./tests/logs1/test1"
        assert files[1] == "./tests/logs1/test2"
        assert files[2] == "./tests/logs2/test3"
        assert files[3] == "./tests/logs2/test4"

    # two words, each matching one file in or mode
    def test_search1(self):
        matched_logs = search(self.files, ["asdf","qwer"], True, False)
        assert matched_logs == ["./tests/logs1/test1","./tests/logs2/test3"]

    # simple case, one file matching one string in and mode
    def test_search2(self):
        matched_logs = search(self.files, ["asdf"], False, False)
        assert matched_logs == ["./tests/logs1/test1"]

    # would match in or mode but doesn't in and mode
    def test_search3(self):
        matched_logs = search(self.files, ["asdf","qwer"], False, False)
        assert matched_logs == []

    # or mode, matching all files
    def test_search4(self):
        matched_logs = search(self.files, ["asdf","qwer","hjk","uiop"], True, False)
        assert matched_logs == ["./tests/logs1/test1","./tests/logs1/test2","./tests/logs2/test3","./tests/logs2/test4"]

    # simple regular expression, matching a single file in and mode
    def test_search5(self):
        matched_logs = search(self.files, ["dfa.*fas"], False, True)
        assert matched_logs == ["./tests/logs1/test1"]

    # simple regular expression, matching a single file in and mode
    def test_search6(self):
        matched_logs = search(self.files, ["dfa.*fas"], False, True)
        assert matched_logs == ["./tests/logs1/test1"]

    # regexps in or mode, matching two files
    def test_search7(self):
        matched_logs = search(self.files, ['hjk...j','qwer.*we'], True, True)
        assert matched_logs == ["./tests/logs1/test2","./tests/logs2/test3"]

    # a more complex regex, exercising MULTILINE with ^ and $
    def test_search8(self):
        matched_logs = search(self.files, ['^uiop[uiop]+uiop$|^qwer.*we$'], True, True)
        assert matched_logs == ["./tests/logs2/test3","./tests/logs2/test4"]

#def setup():
#    content = "# this is a test configuration file\n./tests/logs1/test1\n./tests/logs1/test2\n./tests/logs2/test3\n./tests/logs2/test4"
#    with open('logfind.config.txt','w') as f:
#        f.write(content)
#    self.addCleanup(os.remove, 'logfind.config.txt')
#
#def teardown():
#    print "asdf"
#    with open('logfind.config.txt','r') as f:
#        print f
#    #os.remove('logfind.config.txt')
#
#@with_setup(setup, teardown)
#def test_conf_to_files():
#    print "asdf"

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
