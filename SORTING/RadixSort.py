def radixsort(array):
    length = len(array)
    while length > 1:
        max_element_index = array.index(max(array[0:length]))
        array = array[max_element_index::-1] + array[max_element_index + 1:len(array)]
        array = array[length - 1::-1] + array[length:len(array)]
        length -= 1
    return array
