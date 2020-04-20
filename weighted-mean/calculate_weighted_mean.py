from typing import List


def hacker_rank_input_to_list(raw_input) -> List[int]:
    """
    Converst the hacker rank input to the value they actually use.

    :param raw_input: string separated by space
    :return: list of ints

    """
    return list(map(int, raw_input.split(" ")))


def weighted_mean(number_list: list, weight_list: list, delta_list: int) -> \
        float:
    """
    Performs the weighted mean calculation
    :param number_list: The numbers to calculate the weighted mean
    :param weight_list: The weight of the elements in the list
    :param delta_list: How many elements should the array have
    :return: Decimal
    """

    if len(number_list) != delta_list or len(weight_list) != delta_list:
        return False

    divisor = sum(weight_list)
    dividend = sum([a * b for a, b in zip(number_list, weight_list)])
    return round((dividend / divisor), 1)
