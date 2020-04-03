import logging
from itertools import product

from typing import List


def clean_data(samples: List[str]) -> List[int]:
    return [list(map(int, data)) for data in
            list(map(lambda x: x.split(' ')[1:], samples))
            ]


def maximize_it(samples: List[int], modulo: int) -> int:
    logging.info(f"Received {samples}")
    return max(map(
        lambda x: sum(i**2 for i in x) % modulo, product(*samples))
    )
