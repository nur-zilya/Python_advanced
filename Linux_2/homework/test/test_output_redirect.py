import io
import sys
import unittest

from Linux_2.homework.output_redirect import Redirect

class TestRedirect(unittest.TestCase):
    def test_redirect_stdout(self):
        output = io.StringIO()
        with Redirect(stdout=output):
            print('Hello stdout')
        self.assertEqual(output.getvalue(), 'Hello stdout\n')

    def test_redirect_stderr(self):
        output = io.StringIO()
        with Redirect(stderr=output):
            sys.stderr.write('Hello stderr\n')
        self.assertEqual(output.getvalue(), 'Hello stderr\n')

    def test_redirect_both(self):
        stdout = io.StringIO()
        stderr = io.StringIO()
        with Redirect(stdout=stdout, stderr=stderr):
            print('Hello stdout')
            sys.stderr.write('Hello stderr\n')
        self.assertEqual(stdout.getvalue(), 'Hello stdout\n')
        self.assertEqual(stderr.getvalue(), 'Hello stderr\n')

    def test_no_redirect(self):
        with Redirect():
            print('Hello stdout')
            sys.stderr.write('Hello stderr\n')
        self.assertEqual(sys.stdout, sys.__stdout__)
        self.assertEqual(sys.stderr, sys.__stderr__)

    def test_redirect_only_stdout(self):
        output = io.StringIO()
        with Redirect(stdout=output):
            print('Hello stdout')
            sys.stderr.write('Hello stderr\n')
        self.assertEqual(output.getvalue(), 'Hello stdout\n')
        self.assertEqual(sys.stderr, sys.__stderr__)


if __name__ == "__main__":
    unittest.main()