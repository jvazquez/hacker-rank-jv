import unittest

from merge_the_tools.app import is_factor


class TestMergeTheTools(unittest.TestCase):
    def test_is_factor(self):
        self.assertEqual(True, is_factor(9, 3))

    def test_obtain_number(self):
        target = "AABCAAADA"

if __name__ == '__main__':
    unittest.main()
