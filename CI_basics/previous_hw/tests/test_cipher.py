import unittest

from CI_basics.previous_hw.cipher import decode

class TestDecode(unittest.TestCase):

    def test_decode_abracadabra(self):
        self.assertEqual(decode("абра-кадабра."), "абра-кадабра")

    def test_decode_abra_dots_hyphen(self):
        self.assertEqual(decode("абраа..-кадабра"), "абра-кадабра")

    def test_decode_abra_dots_hyphen_dot(self):
        self.assertEqual(decode("абраа..-.кадабра"), "абра-кадабра")

    def test_decode_abra_hyphens_dots(self):
        self.assertEqual(decode("абра--..кадабра"), "абра-кадабра")

    def test_decode_abrau_dots_hyphen(self):
        self.assertEqual(decode("абрау...-кадабра"), "абра-кадабра")

    def test_decode_only_dots(self):
        self.assertEqual(decode("........"), "")

    def test_decode_dots_and_letter(self):
        self.assertEqual(decode("абр......a."), "a")

    def test_decode_numbers(self):
        self.assertEqual(decode("1..2.3"), "23")

    def test_decode_only_dot(self):
        self.assertEqual(decode("."), "")

    def test_decode_only_ones_and_dots(self):
        self.assertEqual(decode("1......................."), "")
