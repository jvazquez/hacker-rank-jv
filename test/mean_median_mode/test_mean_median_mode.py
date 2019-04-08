import logging
import unittest

from decimal import Decimal, getcontext

from mean_median_mode.app import mean, median, mode
from misc.open_file import get_json

logger = logging.getLogger(__name__)
getcontext().prec = 2


class MeanTestCase(unittest.TestCase):
    # def test_mean_case_one(self):
    #     data = get_json('fixture.json')
    #     input_size = int(data.get('one').get('input_size'))
    #     sample_data = data.get('one').get('elements')
    #     elements = sorted(map(int, sample_data.split(' ')))
    #     result = mean(elements, input_size)
    #     self.assertEqual(result, 51284.9)

    def test_mean_case_three(self):
        data = get_json('fixture.json')
        input_size = int(data.get('three').get('input_size'))
        sample_data = data.get('three').get('elements')
        elements = sorted(map(int, sample_data.split(' ')))
        result = mean(elements, input_size)
        self.assertEqual(round(result, 1), 49921.5)


class MedianTestCase(unittest.TestCase):
    # def test_mean_case_one(self):
    #     data = get_json('fixture.json')
    #     sample_data = data.get('one').get('elements')
    #     elements = sorted(map(int, sample_data.split(' ')))
    #     input_size = int(data.get('one').get('input_size'))
    #     result = median(elements, input_size)
    #     self.assertEqual(result, 51113.0)

    def test_mean_case_three(self):
        data = get_json('fixture.json')
        sample_data = data.get('three').get('elements')
        elements = sorted(map(int, sample_data.split(' ')))
        input_size = int(data.get('three').get('input_size'))
        result = median(elements, input_size)
        self.assertEqual(result, 49253.5)


class ModeTestCase(unittest.TestCase):
    # def test_mode_case_one(self):
    #     data = get_json('fixture.json')
    #     sample_data = data.get('one').get('elements')
    #     elements = sorted(map(int, sample_data.split(' ')))
    #     result = mode(elements)
    #     self.assertEqual(result, 6392)

    def test_mode_case_three(self):
        data = get_json('fixture.json')
        sample_data = data.get('three').get('elements')
        elements = sorted(map(int, sample_data.split(' ')))
        result = mode(elements)
        self.assertEqual(result, 2184)


if __name__ == '__main__':
    unittest.main()
