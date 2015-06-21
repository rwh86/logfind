from nose.tools import *
from logfind.logfind import *
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

    def test_search1(self):
        matched_logs = search(self.files, ["asdf","qwer"], 'or')
        assert matched_logs == ["./tests/logs1/test1","./tests/logs2/test3"]

    def test_search2(self):
        matched_logs = search(self.files, ["asdf"], 'and')
        assert matched_logs == ["./tests/logs1/test1"]

    def test_search3(self):
        matched_logs = search(self.files, ["asdf","qwer"], 'and')
        assert matched_logs == []

    def test_search4(self):
        matched_logs = search(self.files, ["asdf","qwer","hjk","uiop"], 'or')
        assert matched_logs == ["./tests/logs1/test1","./tests/logs1/test2","./tests/logs2/test3","./tests/logs2/test4"]



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
