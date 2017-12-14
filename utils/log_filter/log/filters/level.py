'''
Created on Mar 25, 2016

@author: jvazquez
'''
import logging


class SingleLevelFilter(logging.Filter):
    def __init__(self, passlevel, reject):
        """
        We specify a custom filter to only log
        certain log levels

        params
          passlevel int Use the values from logging.LEVEL ints
          reject boolean the filter value
        """

        self.passlevel = passlevel
        self.reject = reject

    def filter(self, record):
        """
        Filter implementation.
        It will only log what we define we should log

        params
          record LogRecord A log record object
        return
          boolean
        """
        if self.reject:
            return (record.levelno != self.passlevel)
        else:
            return (record.levelno == self.passlevel)
