import unittest
from unittest.mock import patch
from CI_basics.previous_hw import cipher

class TestDecode(unittest.TestCase):
    @patch('builtins.input', side_effect=['абра-кадабра.'])
    def test_decode(self, mock_input):
        test_cases = [
            ('абра-кадабра.', 'абра-кадабра'),
            ('абраа..-кадабра', 'абра-кадабра'),
            ('абраа..-.кадабра', 'абра-кадабра'),
            ('абра--..кадабра', 'абра-кадабра'),
            ('абрау...-кадабра', 'абра-кадабра'),
            ('абра........', ''),
            ('абр......a.', 'a'),
            ('1..2.3', '23'),
            ('.', ''),
            ('1.......................', ''),
        ]

        for cipher, expected in test_cases:
            with self.subTest(cipher=cipher, expected=expected):
                self.assertEqual(cipher.decode(cipher), expected)

if __name__ == "__main__":
    unittest.main()
