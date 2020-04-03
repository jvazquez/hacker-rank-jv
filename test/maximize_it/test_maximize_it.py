import logging
import sys
import unittest

from maximize_it.app import clean_data, maximize_it

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


class TestMaximizeIt(unittest.TestCase):
    def test_case_zero(self):
        expected = 206
        elements, modulo = map(int, '3 100'.split(' '))
        total_lists = clean_data(['2 5 4', '3 7 8 9', '5 5 7 8 9 10'])
        self.assertEqual(expected, maximize_it(total_lists, modulo))

    def test_case_two(self):
        elements, modulo = map(int, '7 867'.split(' '))
        expected = 866
        total_lists = clean_data([
            '7 6429964 4173738 9941618 2744666 5392018 5813128 9452095',
            '7 6517823 4135421 6418713 9924958 9370532 7940650 2027017',
            '7 1506500 3460933 1550284 3679489 4538773 5216621 5645660',
            '7 7443563 5181142 8804416 8726696 5358847 7155276 4433125',
            '7 2230555 3920370 7851992 1176871 610460 309961 3921536',
            '7 8518829 8639441 3373630 5036651 5291213 2308694 7477960',
            '7 7178097 249343 9504976 8684596 6226627 1055259 4880436'
        ])
        self.assertEqual(expected, maximize_it(total_lists, modulo))


if __name__ == '__main__':
    unittest.main()
