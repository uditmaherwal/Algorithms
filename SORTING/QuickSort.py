def quicksort(array_of_elements):
    length = len(array_of_elements)
    if length <= 1:
        return
    pivot = array_of_elements.pop()
    lesser, greater = [],[]
    for element in array_of_elements:
        if element > pivot:
            greater.append(element)
        else:
            lesser.append(element)

    return quicksort(lesser) + [pivot] + quicksort(greater)
