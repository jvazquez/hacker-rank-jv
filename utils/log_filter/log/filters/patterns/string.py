'''
Created on Mar 25, 2016

@author: jvazquez
'''
import logging


class StringLevelFilter(logging.Filter):
    def __init__(self, pattern_accepted, passlevel, reject):
        """
        We specify a custom filter to only log
        certain log levels

        params
          pattern_accepted string A regular expression of the type of file
                           that may invoke this class. If it's the right kind,
                           we will log
          passlevel int Use the values from logging.LEVEL ints
          reject boolean the filter value
        """

        self.pattern_accepted = pattern_accepted
        self.passlevel = passlevel
        self.reject = reject

    def filter(self, record):
        """
        Filter implementation.
        It will only log if the pattern_accepted is part of the invoker
        _record.name_ and the pattern level is the expected
        For example, only log if the module name contains the name
        test and the loglevel accepted is DEBUG (10)
        params
          record LogRecord A log record object
        return
          boolean
        """

        if self.reject:
            return (record.levelno != self.passlevel)
        else:
            return (record.levelno == self.passlevel and
                    self.pattern_accepted in record.name)
