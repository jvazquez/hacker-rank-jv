import unittest
import logging

import unittest

from collections import deque

from calculate_weighted_mean import weighted_mean


logger = logging.getLogger(__name__)


class WeightedMeanTestCase(unittest.TestCase):
    def test_list_sanity_with_a_bigger_delta(self):
        delta = 6
        number_list = [10, 40, 30, 50, 20]
        weight_list = [1, 2, 3, 4, 5]
        self.assertFalse(weighted_mean(number_list, weight_list, delta))

    def test_list_sanity_with_a_lower_delta(self):
        delta = 4
        number_list = [10, 40, 30, 50, 20]
        weight_list = [1, 2, 3, 4, 5]
        self.assertFalse(weighted_mean(number_list, weight_list, delta))

    def test_formula_first_case(self):
        delta = 5
        number_list = [10, 40, 30, 50, 20]
        weight_list = [1, 2, 3, 4, 5]
        self.assertEqual(weighted_mean(number_list, weight_list, delta), 32.0)


if __name__ == '__main__':
    unittest.main()
