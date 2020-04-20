import unittest
from counting_valleys.valley_counter import counting_valleys


class TestCountingValleys(unittest.TestCase):
    def test_valley_count_case_zero(self):
        steps = 8
        pattern = "UDDDUDUU"
        expected = 1
        self.assertEqual(expected, counting_valleys(steps, pattern))

    def test_valley_count_case_one(self):
        steps = 12
        pattern = "DDUUDDUDUUUD"
        expected = 2
        self.assertEqual(expected, counting_valleys(steps, pattern))


if __name__ == '__main__':
    unittest.main()
