import unittest

from repeated_string.string_repeater import repeated_string


class TestStringRepeater(unittest.TestCase):
    def test_sample_case(self):
        random_string = "abcac"
        random_number = 10
        expected = 4
        a_count = repeated_string(random_string, random_number)
        self.assertEqual(expected, a_count)

    def test_sample_case_two(self):
        random_string = "aba"
        random_number = 10
        expected = 7
        a_count = repeated_string(random_string, random_number)
        self.assertEqual(expected, a_count)


if __name__ == '__main__':
    unittest.main()
