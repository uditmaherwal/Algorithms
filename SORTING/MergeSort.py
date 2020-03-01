def mergesort(array):
    def merge(left_array, right_array):
        result_array = []
        while left_array and right_array :
            result_array.append((left_array if left_array[0] < right_array[0] else right_array).pop(0))
        return result_array + left_array + right_array

    if len(array) <= 1 :
        return array
    mid = len(array) // 2
    return merge(mergesort(array[:mid]),mergesort(array[mid:]))
