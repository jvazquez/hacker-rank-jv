import unittest

from leap_year.app import is_leap_year


class TestLeapYearCase(unittest.TestCase):
    def test_detect_is_leap_year(self):
        year = 1990
        self.assertFalse(is_leap_year(year))
        year = 1992
        self.assertTrue(is_leap_year(year))


if __name__ == '__main__':
    unittest.main()
