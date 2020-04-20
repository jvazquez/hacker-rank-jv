import unittest

from .cloud_jumper import cloud_jumper
from utils.input_converter import ugly_to_list


class TestCloudJumper(unittest.TestCase):
    def test_sample_scenario(self):
        expected = 3
        cloud_list = ugly_to_list("0 0 0 0 1 0")
        jumps = cloud_jumper(cloud_list)
        self.assertEqual(expected, jumps)


if __name__ == '__main__':
    unittest.main()
