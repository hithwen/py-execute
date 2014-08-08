'''
Created on 19/06/2013

@author: drodri
'''
import unittest
from StringIO import StringIO
import platform
from py_execute.process_executor import execute
from py_execute.basicuserio import BasicUserIO
from py_execute.outputstream_wrapper import OutputStreamWrapper
import sys
from nose.plugins.attrib import attr


@attr('integration')
class TestProcessExecutor(unittest.TestCase):

    def test_process_executor(self):
        ui = BasicUserIO(sys.stdin, out=OutputStreamWrapper(StringIO()))
        if platform.system() == 'Windows':
            command = 'ping 127.0.0.1 -n 1'
            shell = False
        else:
            command = 'ping -c 1 127.0.0.1'
            shell = True

        r, o = execute(command, ui, shell=shell)

        self.assertEqual(0, r)
        self.assertIn('127.0.0.1', o)
        self.assertIn('127.0.0.1', str(ui.out))

    '''def testMassiveWindows(self):

        p = process_executor()
        ui = UserIO(Mock(), out=BiiOutputStream(sys.stdout))
        if platform.system() == 'Windows':
            command = 'python pum'

            r, o, e = p.execute(command, ui)

            print r
            print o
            print e'''


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
