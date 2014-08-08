'''
Created on 03/07/2013

@author: julia
'''
from unittest import TestCase
from biicode.lib.process_executor.outputstream_wrapper import OutputStreamWrapper
from StringIO import StringIO
import tempfile
import re

DEBUG = 0
INFO = 1
WARN = 2
ERROR = 3


class TestBiiOutputStream(TestCase):
    def setUp(self):
        _, self.log_file = tempfile.mkstemp()
        self.outstring = StringIO()
        self.out = OutputStreamWrapper(stream=self.outstring, log_file_name=self.log_file)

    def test_write(self):
        self.out.write('hello')
        self.assertEquals('hello', self.outstring.getvalue())
        with open(self.log_file) as log:
            regex = '.* INFO: hello\n'
            a = re.compile(regex)
            content = log.read()
            self.assertTrue(a.match(content), '%s does not match regex' % content)

    def test_log(self):
        self.out.log('debug')  # Debug logs do not show on normal output
        self.out.log('info', INFO)
        self.out.log('warn', WARN)
        self.out.log('error', ERROR)
        self.assertEquals('INFO: info\nWARN: warn\nERROR: error\n',
                          self.outstring.getvalue())
        with open(self.log_file) as log:
            regex = '.* DEBUG: debug\n.* INFO: info\n.* WARNING: warn\n.* ERROR: error'
            a = re.compile(regex)
            content = log.read()
            print content
            self.assertTrue(a.match(content), '%s does not match regex' % content)
