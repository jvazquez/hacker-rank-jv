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

from anagrams.app import number_needed


class TestAnagram(unittest.TestCase):

    def test_number_needed_sample(self):
        word_a = 'cde'
        word_b = 'abc'
        expected = 4
        number = number_needed(word_a, word_b)
        self.assertEqual(expected, number)

    def test_number_needed_case_one(self):
        word_a = 'fcrxzwscanmligyxyvym'
        word_b = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'
        expected = 30
        number = number_needed(word_a, word_b)
        self.assertEqual(expected, number)
