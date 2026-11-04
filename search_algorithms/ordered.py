from collections.abc import Sequence


def binary_search(items: Sequence[int], target: int) -> int:
    """Return any matching index in an ascendingly sorted sequence, or -1."""
    low, high = 0, len(items) - 1
    while low <= high:
        middle = (low + high) // 2
        if items[middle] == target:
            return middle
        if items[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1


def jump_search(items: Sequence[int], target: int) -> int:
    """Search a sorted sequence by fixed-size blocks, then scan one block."""
    size = len(items)
    if not size:
        return -1
    step = max(1, int(size**0.5))
    start, end = 0, step
    while start < size and items[min(end, size) - 1] < target:
        start, end = end, end + step
    for index in range(start, min(end, size)):
        if items[index] == target:
            return index
        if items[index] > target:
            break
    return -1


def interpolation_search(items: Sequence[int], target: int) -> int:
    """Search roughly uniformly distributed sorted integers."""
    low, high = 0, len(items) - 1
    while low <= high and items[low] <= target <= items[high]:
        if items[low] == items[high]:
            return low if items[low] == target else -1
        position = low + (target - items[low]) * (high - low) // (
            items[high] - items[low]
        )
        if items[position] == target:
            return position
        if items[position] < target:
            low = position + 1
        else:
            high = position - 1
    return -1


def exponential_search(items: Sequence[int], target: int) -> int:
    """Find a bounded range exponentially, then binary search that range."""
    size = len(items)
    if not size:
        return -1
    if items[0] == target:
        return 0
    bound = 1
    while bound < size and items[bound] < target:
        bound *= 2
    low, high = bound // 2, min(bound, size - 1)
    while low <= high:
        middle = (low + high) // 2
        if items[middle] == target:
            return middle
        if items[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1


def fibonacci_search(items: Sequence[int], target: int) -> int:
    """Search a sorted sequence using Fibonacci-sized offsets."""
    size = len(items)
    fib_previous, fib_current = 0, 1
    fib_next = fib_previous + fib_current
    while fib_next < size:
        fib_previous, fib_current = fib_current, fib_next
        fib_next = fib_previous + fib_current

    offset = -1
    while fib_next > 1:
        index = min(offset + fib_previous, size - 1)
        if items[index] < target:
            fib_next, fib_current = fib_current, fib_previous
            fib_previous = fib_next - fib_current
            offset = index
        elif items[index] > target:
            fib_next, fib_current = fib_previous, fib_current - fib_previous
            fib_previous = fib_next - fib_current
        else:
            return index
    next_index = offset + 1
    if fib_current and next_index < size and items[next_index] == target:
        return next_index
    return -1


def ternary_search(items: Sequence[int], target: int) -> int:
    """Search a sorted sequence by repeatedly splitting its range in thirds."""
    low, high = 0, len(items) - 1
    while low <= high:
        third = (high - low) // 3
        first, second = low + third, high - third
        if items[first] == target:
            return first
        if items[second] == target:
            return second
        if target < items[first]:
            high = first - 1
        elif target > items[second]:
            low = second + 1
        else:
            low, high = first + 1, second - 1
    return -1
