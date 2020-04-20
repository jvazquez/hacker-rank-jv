from typing import List


def ugly_to_list(string_split_by_spaces: str) -> List:
    return string_split_by_spaces.rstrip().split()
