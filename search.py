from collections.abc import Sequence
from typing import TypeVar


T = TypeVar("T")


def linear_search(items: Sequence[T], target: T) -> int:
    """Return the index of the first matching item, or -1 if it is absent."""
    for index, item in enumerate(items):
        if item == target:
            return index
    return -1


if __name__ == "__main__":
    numbers = [10, 23, 45, 70, 11, 15]
    target = 70
    result = linear_search(numbers, target)

    if result == -1:
        print(f"{target} was not found.")
    else:
        print(f"{target} was found at index {result}.")