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
import json
import os
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

    def test_number_needed_case_two(self):
        word_a = 'bugexikjevtubidpulaelsbcqlupwetzyzdvjphn'
        word_b = 'lajoipfecfinxjspxmevqxuqyalhrsxcvgsdxxkacspbchrbvvwnvsdtsrdk'
        expected = 40
        number = number_needed(word_a, word_b)
        self.assertEqual(expected, number)

    def test_number_needed_case_five(self):
        cases_file = os.path.abspath(
            os.path.join(os.path.dirname(__file__),
                         'cases.json')
            )

        with open(cases_file, 'r') as test_case:
            payload = json.loads(test_case.read())

        word_a = payload['5']['a']
        word_b = payload['5']['b']
        expected = 1000
        number = number_needed(word_a, word_b)
        self.assertEqual(expected, number)

    def test_number_needed_case_six(self):
        cases_file = os.path.abspath(
            os.path.join(os.path.dirname(__file__),
                         'cases.json')
            )

        with open(cases_file, 'r') as test_case:
            payload = json.loads(test_case.read())

        word_a = payload['6']['a']
        word_b = payload['6']['b']
        expected = 596
        number = number_needed(word_a, word_b)
        self.assertEqual(expected, number)
