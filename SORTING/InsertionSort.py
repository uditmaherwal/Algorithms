def inserstionsort(array):
    length = len(array)
    for marker in range(1,length):
        marker_setter = marker
        while(marker_setter > 0 and array[marker_setter - 1] > array[marker_setter]):
            array[marker_setter],array[marker] = array[marker],array[marker_setter]
            marker_setter -= 1
    return array
