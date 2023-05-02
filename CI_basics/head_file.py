import unittest
import os

def head_file(file_path, num_lines):
    """
    Returns the first `num_lines` of a file at the given `file_path`.
    Returns 404 if file does not exist or is a binary file.
    """
    if not os.path.isfile(file_path):
        return 404

    # Check if file is binary
    with open(file_path, 'rb') as f:
        try:
            f.read().decode('utf-8')
        except UnicodeDecodeError:
            return 404

    # Read the first `num_lines` of the file
    with open(file_path, 'r') as f:
        return 200, ''.join([next(f) for _ in range(num_lines)])

class TestHeadFile(unittest.TestCase):
    def setUp(self):
        with open('test.txt', 'w') as f:
            f.write('Line 1\nLine 2\nLine 3\nLine 4\nLine 5\n')

    def tearDown(self):
        os.remove('test.txt')

    def test_empty_file(self):
        with open('empty.txt', 'w') as f:
            pass
        self.assertEqual(head_file('empty.txt', 3), (200, ''))

    def test_file_not_exists(self):
        self.assertEqual(head_file('not_exists.txt', 3), 404)

    def test_binary_file(self):
        with open('binary.png', 'wb') as f:
            f.write(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR...')
        self.assertEqual(head_file('binary.png', 3), 404)

    def test_valid_file(self):
        self.assertEqual(head_file('test.txt', 3), (200, 'Line 1\nLine 2\nLine 3\n'))
