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


def letter_filter(pivot):
    while True:
        outside_letter = yield
        if outside_letter not in pivot:
            yield outside_letter


def number_needed(word_a, word_b):
    """Determine the amount of chars needed to
    be deleted in order to conform an anagram

    Parameters:
        word_a `string`
        word_b `string`
    Returns
        `int`

    """

    word_a_len = len(word_a)
    word_b_len = len(word_b)
    bucket = []

    if word_a_len > word_b_len:
        scanner = letter_filter(word_a)
        next(scanner)
        for letter in word_b:
            popped = scanner.send(letter)
            if popped is not None:
                bucket.append(popped)

        new_a = [letter for letter in word_a if letter not in bucket]
        return len(new_a)
    elif word_b_len > word_a_len:
        scanner = letter_filter(word_b)
        next(scanner)
        for letter in word_a:
            popped = scanner.send(letter)
            if popped is not None:
                bucket.append(popped)

        new_b = [letter for letter in word_b if letter not in bucket]
        return len(new_b)
    elif word_b_len == word_a_len:
        bucket_a = [letter for letter in word_a if letter not in word_b]
        bucket_b = [letter for letter in word_b if letter not in word_a]
        return len(bucket_a + bucket_b)
