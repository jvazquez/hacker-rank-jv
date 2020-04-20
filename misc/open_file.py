# -*- coding: utf-8 -*-
"""
:mod:`open_file` -- Open a file with generators
===================================

.. module:: open_file
   :platform: Unix, Windows
   :synopsis: I recall an example where they asked me to open a file,
   but instead of opening the file and read line by line, they
   wanted me to do something different.
.. moduleauthor:: Jorge Omar Vazquez <jorgeomar.vazquez@gmail.com>
..:date: Dec 30, 2017
"""
import json
import logging
import os

import logconfig

TARGET = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                      'sample.txt'))
_LOG = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    '../logging.json'))
logconfig.from_json(_LOG)

logger = logging.getLogger('debug')


def get_json(filename):
    """
    Return json data from a file
    :param filename:str path
    :return: dict
    """
    with obtain_stream(filename) as stream:
        data = json.loads(stream.read())
    return data


def obtain_stream(target):
    return open(target, 'r')


def read_file(stream):
    while True:
        data = stream.readline()
        if not data:
            break
        yield data


def word_handler(word):
    return 'e' in word


try:
    with obtain_stream(TARGET) as content:
        for word in read_file(content):
            map(word_handler, word.split(' '))
except Exception:
    logger.exception("We had error")
