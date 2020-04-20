from utils.input_converter import ugly_to_list


def repeated_string(random_string: str, random_number: int) -> int:
    # My solution was ugly, but I can't simply understand the criteria of the
    # problem.
    # The accepted solution doesn't even completes the string up to n characters
    # like the problem says
    return random_string.count("a") * \
           (random_number // len(random_string)) + \
           random_string[:random_number % len(random_string)].count("a")
