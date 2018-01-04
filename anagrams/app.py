# -*- coding: utf-8 -*-
"""
:mod:`app` -- Anagram solver
===================================

.. module:: app
   :platform: Unix, Windows
   :synopsis: Determines the amount of letters needed to be
removed from two strings so they becom anagrams
.. moduleauthor:: Jorge Omar Vazquez <jorgeomar.vazquez@gmail.com>
..:date: Dec 28, 2017
"""
import logging

logger = logging.getLogger("debug")


def letter_counter(pivot_word):
    letter_container = dict()

    for letter in pivot_word:
        if letter not in letter_container.keys():
            letter_container[letter] = 1
        else:
            letter_container[letter] += 1

    return letter_container


def number_needed(word_a, word_b):
    """Determine the amount of chars needed to
    be deleted in order to conform an anagram

    Parameters:
        word_a `string`
        word_b `string`
    Returns
        `int`

    """

    bucket_a = letter_counter(word_a)
    bucket_b = letter_counter(word_b)
    delete_values = 0
    set_a = set(bucket_a)
    set_b = set(bucket_b)

    for letter in (set_b ^ set_a):
        if letter in bucket_a.keys():
            delete_values += bucket_a[letter]
        elif letter in bucket_b.keys():
            delete_values += bucket_b[letter]

    for letter in set_a.intersection(set_b):
        if bucket_a[letter] > bucket_b[letter]:
            increment = bucket_a[letter] - bucket_b[letter]
            delete_values += increment
        elif bucket_b[letter] > bucket_a[letter]:
            increment = bucket_b[letter] - bucket_a[letter]
            delete_values += increment

    return delete_values
