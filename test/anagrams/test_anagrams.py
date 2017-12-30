# -*- coding: utf-8 -*-
"""
:mod:`test_anagrams` -- Test the validity of anagrams and helper functions
===================================

.. module:: test_anagrams
   :platform: Unix, Windows
   :synopsis: Test the validity of anagrams
.. moduleauthor:: Jorge Omar Vazquez <jorgeomar.vazquez@gmail.com>
..:date: Dec 28, 2017
"""

import unittest

from collections import deque

from anagrams.app import number_needed, proper_len


class TestAnagram(unittest.TestCase):


    def test_empty_string_does_not_have_proper_len(self):
        self.assertFalse(proper_len(''))

    def test_none_does_not_have_proper_len(self):
        self.assertFalse(None)

    def test_long_string_does_not_have_proper_len(self):
        sample = deque(map(lambda x: x*pow(10, 5), "x"))
        self.assertFalse(proper_len(sample[0]))

    def test_number_needed_obtains_required_number(self):
        word_a = 'cde'
        word_b = 'abc'
        expected = 4
        number = number_needed(word_a, word_b)
        self.assertTrue(type(number) == type(1))
        self.assertEqual(expected, number)

    def test_number_needed_case_one(self):
        word_a = 'fcrxzwscanmligyxyvym'
        word_b = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'
        expected = 30
        number = number_needed(word_a, word_b)
        self.assertEqual(expected, number)
