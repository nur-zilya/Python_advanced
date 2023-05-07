import unittest
import datetime

from CI_basics.Person import Person

class TestPerson(unittest.TestCase):
        def test_init(self):
            p = Person('John', 2000, 'London')
            self.assertEqual(p.name, 'John')
            self.assertEqual(p.yob, 2000)
            self.assertEqual(p.address, 'London')

        def test_get_age(self):
            p = Person('John', 2000)
            current_year = datetime.datetime.now().year
            expected_age = current_year - p.yob
            self.assertEqual(p.get_age(), expected_age)

        def test_get_name(self):
            p = Person('John', 2000)
            self.assertEqual(p.get_name(), 'John')

        def test_set_name(self):
            p = Person('John', 2000)
            p.set_name('Jane')
            self.assertEqual(p.get_name(), 'Jane')

        def test_set_address(self):
            p = Person('John', 2000, 'London')
            p.set_address('New York')
            self.assertEqual(p.get_address(), 'New York')

        def test_get_address(self):
            p = Person('John', 2000, 'London')
            self.assertEqual(p.get_address(), 'London')

        def test_is_homeless(self):
            p1 = Person('John', 2000, 'London')
            self.assertFalse(p1.is_homeless())
            p2 = Person('Jane', 2001)
            self.assertTrue(p2.is_homeless())


if __name__ == "__main__":
    unittest.main()
