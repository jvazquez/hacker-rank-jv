"""
https://algs4.cs.princeton.edu/14analysis/ThreeSum.java.html

A program with cubic running time. Reads pairs integers
and counts the number of triples that sum to exactly 0
(ignoring integer overflow).
"""
import sys
from sedgewick_ports.utils.resource_loader import resource_path

VALID_FILES = {
    "1kints": resource_path("1Kints.txt"),
    "8kints": resource_path("8Kints.txt"),
    "16kints": resource_path("16Kints.txt"),
    "32kints": resource_path("32Kints.txt"),
    "1mints": resource_path("1Mints.txt"),
}


class InvalidResourceException(Exception):
    pass


def run(target):
    print(f"Reading file {target}")

    with open(VALID_FILES.get(target)) as fp:
        data = fp.read()

    """
    for (int i = 0; i < pairs; i++) {
            for (int j = i+1; j < pairs; j++) {
                for (int k = j+1; k < pairs; k++) {
                    if (a[i] + a[j] + a[k] == 0) {
                        count++;
                    }
                }
            }
        }
    """
    i = 0
    n = len(data)
    while i < n:
        j = i + n
        while j < n:
            k = j + 1
            while k < n:
                if data[i] + data[j] + data[k] == 0:
                    print(f"{data[i]} {data[j]} {data[k]}")
                k += 1
                j += 1
                i += 1


if __name__ == "__main__":
    try:
        sample_file = sys.argv[1]
        if sample_file not in VALID_FILES.keys():
            raise InvalidResourceException("Invalid resource provided.")
        run(sample_file)
    except IndexError:
        print("You need to provide a sample filename")
        sys.exit(-1)
    except InvalidResourceException:
        print(f'The only two resources are {",".join(VALID_FILES.keys())}')
        sys.exit(-1)
