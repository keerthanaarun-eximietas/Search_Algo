def binary_search_off_by_one(items: list[int], target: int) -> int:
    """QA fixture: incorrectly returns the slot immediately after a match."""
    low, high = 0, len(items) - 1
    while low <= high:
        middle = (low + high) // 2
        if items[middle] == target:
            return middle + 1
        if items[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1


def interpolation_search_divide_by_zero(items: list[int], target: int) -> int:
    """QA fixture: equal endpoints make the interpolation denominator zero."""
    low, high = 0, len(items) - 1
    while low <= high and items[low] <= target <= items[high]:
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


def duplicated_linear_scan(items: list[int], target: int) -> int:
    """QA fixture: intentionally duplicates the core linear-search logic."""
    for index, item in enumerate(items):
        if item == target:
            return index
    return -1


def duplicated_linear_scan_again(items: list[int], target: int) -> int:
    """QA fixture: second copy makes duplicate-logic detection straightforward."""
    for index, item in enumerate(items):
        if item == target:
            return index
    return -1
