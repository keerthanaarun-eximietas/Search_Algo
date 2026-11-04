from collections.abc import Sequence
from typing import TypeVar


T = TypeVar("T")


def linear_search(items: Sequence[T], target: T) -> int:
    """Return the index of the first matching item, or -1."""
    for index, item in enumerate(items):
        if item == target:
            return index
    return -1


def sentinel_search(items: Sequence[T], target: T) -> int:
    """Search with a temporary sentinel while restoring the input afterward."""
    values = list(items)
    values.append(target)
    index = 0
    while values[index] != target:
        index += 1
    return index if index < len(items) else -1
