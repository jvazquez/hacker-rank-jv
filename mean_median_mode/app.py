import logging
import math

logger = logging.getLogger(__name__)


def mean(elements, input_size):
    return sum(elements) / input_size


def median(elements, total_input):
    if total_input % 2 != 0:
        pos = round((total_input - 1) / 2)
        return elements[pos]
    else:
        first = math.floor((total_input - 1) / 2)
        second = round(total_input / 2)
        return (elements[first] + elements[second]) / 2


def mode(elements):
    freq = {}

    for number in elements:
        if number in freq:
            freq_value = freq[number] + 1
            freq.update({number: freq_value})
        else:
            freq[number] = 1

    mode_result = list(filter(lambda pair: pair[1] > 1, freq.items()))
    if len(mode_result):
        return mode_result[0][0]
    else:
        return elements[0]
