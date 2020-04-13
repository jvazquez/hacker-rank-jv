from itertools import zip_longest


def is_factor(number, factor) -> bool:
    return number % factor == 0


def remove_duplicates(sub_segment: str) -> str:
    buffer = set()
    output = []
    for char in sub_segment:
        if char not in buffer:
            output.append(char)
            buffer.add(char)
    return "".join(output)


def groupper(target_string: str, sub_segments: int):
    args = [iter(target_string)] * sub_segments
    for sub_segment in zip_longest(*args):
        yield remove_duplicates(sub_segment)
