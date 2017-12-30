# -*- coding: utf-8 -*-
"""
:mod:`module-name-here` -- Description here 
===================================

.. module:: module-name-here
   :platform: Unix, Windows
   :synopsis: complete.
.. moduleauthor:: Jorge Omar Vazquez <jorgeomar.vazquez@gmail.com>
..:date: Dec 28, 2017
"""

def proper_len(word):
    """Validate the constraints of string length

    Parameters:
        word `string`

    Returns
        `boolean` if string is according to range

    """
    return len(word)>= 1 and len(word) <= pow(10, 4)


def number_needed(word_a, word_b):
    """Determine the amount of chars needed to
    be deleted in order to conform an anagram

    Parameters:
        word_a `string`
        word_b `string`
    Returns
        `int`

    """
    diff_a = set(list(word_a)) - set(list(word_b))
    diff_b = set(list(word_b)) - set(list(word_a))
    return len(diff_b) + len(diff_a)
