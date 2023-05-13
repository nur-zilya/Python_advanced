import unittest

from Linux_2.homework.contex_manager import BlockErrors

class TestBlockErrors(unittest.TestCase):

    def test_block_errors(self):
        err_types = (ZeroDivisionError, TypeError)
        with BlockErrors(err_types):
            a = 1 / 0
        self.assertTrue(True)

    def test_raise_errors(self):
        err_types = (ValueError, TypeError)
        with self.assertRaises(TypeError):
            with BlockErrors(err_types):
                raise TypeError()

    def test_pass_errors(self):
        err_types = (ValueError, TypeError)
        with BlockErrors(err_types):
            pass
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()