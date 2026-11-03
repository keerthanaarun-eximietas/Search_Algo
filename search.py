from collections.abc import Sequence
from typing import TypeVar


T = TypeVar("T")


def linear_search(items: Sequence[T], target: T) -> int:
    """Return the index of the first matching item, or -1 if it is absent."""
    for index, item in enumerate(items):
        if item == target:
            return index
    return -1


def binarySearch(items: Sequence[int], target: int) -> int:
    """Return the index of target in an ascendingly sorted sequence, or -1."""
    low = 0
    high = len(items) - 1

    while low <= high:
        middle = (low + high) // 2
        value = items[middle]

        if value == target:
            return middle
        if value < target:
            low = middle + 1
        else:
            high = middle - 1

    return -1


if __name__ == "__main__":
    numbers = [10, 23, 45, 70, 11, 15]
    target = 70
    result = linear_search(numbers, target)

    if result == -1:
        print(f"{target} was not found.")
    else:
        print(f"{target} was found at index {result}.")

    sorted_numbers = [10, 11, 15, 23, 45, 70]
    binary_result = binarySearch(sorted_numbers, target)
    if binary_result == -1:
        print(f"{target} was not found in the sorted list.")
    else:
        print(f"{target} was found in the sorted list at index {binary_result}.")
        