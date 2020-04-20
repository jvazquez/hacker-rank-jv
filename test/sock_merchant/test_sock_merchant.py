import unittest

from sock_merchant.app import sockMerchant
from utils.input_converter import ugly_to_list


class TestSockMerchant(unittest.TestCase):
    def test_finds_result(self):
        expected = 4
        sockets_list = ugly_to_list("1 1 3 1 2 1 3 3 3 3")
        result = sockMerchant(10, sockets_list)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
