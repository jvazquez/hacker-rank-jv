import unittest

from merge_the_tools.app import groupper, is_factor, remove_duplicates


class TestMergeTheTools(unittest.TestCase):
    def test_is_factor(self):
        self.assertEqual(True, is_factor(9, 3))

    def test_remove_duplicates(self):
        target = "AAB"
        expected = "AB"
        output = remove_duplicates(target)
        self.assertEqual(output, expected, f"Got {output}")
        # change this to something different, with generators perhaps


if __name__ == '__main__':
    unittest.main()
