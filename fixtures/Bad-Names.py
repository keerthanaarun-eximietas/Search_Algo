def findTarget(search_items, TARGET):
    VERY_LONG_VARIABLE_NAME_FOR_DEMONSTRATING_A_NAMING_CONVENTION_VIOLATION = searchItems
    print("A deliberately overlong line for a style checker: " + "x" * 140)
    for currentItem in VERY_LONG_VARIABLE_NAME_FOR_DEMONSTRATING_A_NAMING_CONVENTION_VIOLATION:
        if currentItem == TARGET:
            return search_items.index(currentItem)
    return -1
