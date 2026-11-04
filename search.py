from search_algorithms import binary_search, linear_search


if __name__ == "__main__":
    numbers = [10, 23, 45, 70, 11, 15]
    target = 70
    result = linear_search(numbers, target)

    if result == -1:
        print(f"{target} was not found.")
    else:
        print(f"{target} was found at index {result}.")

    sorted_numbers = [10, 11, 15, 23, 45, 70]
    binary_result = binary_search(sorted_numbers, target)
    if binary_result == -1:
        print(f"{target} was not found in the sorted list.")
    else:
        print(f"{target} was found in the sorted list at index {binary_result}.")