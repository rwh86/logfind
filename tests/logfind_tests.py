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
    def setUp(self):
        content = "# this is a test configuration file\n./tests/logs1/test1\n./tests/logs1/test2\n./tests/logs2/test3\n./tests/logs2/test4"
        with open('logfind.config.txt','w') as f:
            f.write(content)

    def tearDown(self):
        os.remove('logfind.config.txt')
      
    def test_conf_to_files(self):
        files = conf_to_files('logfind.config.txt')
        assert files[0] == "./tests/logs1/test1"

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
