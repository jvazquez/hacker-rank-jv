from math import floor


def is_in_list(number, array):
    return number < len(array)


def find(prime_list, target_number):
    min_number = 0
    max_number = len(prime_list) + 1
    try:
        while min_number <= max_number:
            guess = floor((min_number + max_number) / 2)
            print(f"Did {min_number} + {max_number} / 2 == {guess}")
            if is_in_list(guess, prime_list) and \
                    prime_list[guess] == target_number:
                return guess
            elif is_in_list(guess, prime_list) and \
                    prime_list[guess] < target_number:
                min_number = guess + 1
                print(f"{prime_list[guess]} is minor than {target_number}."
                      f"Array index is at {guess}\n"
                      f"Incrementing array index + 1 = {min_number}\n")
            else:
                max_number = guess - 1
                print(f"{target_number} is major than {prime_list[guess]}."
                      f"Decreasing array index - 1 {max_number}\n")
    except IndexError:
        print(f"Index out of bounds ({guess}), target not found")
    return -1


if __name__ == "__main__":
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
              41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
              89, 97]
    target = 98
    index = find(primes, target)
    if index == -1:
        print(f"{target} not found in primes")
    else:
        print(f"Found {target} at {index}")
