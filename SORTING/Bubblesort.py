def bubblesort(array):
    length = len(array)-1
    for i in range(length,0,-1):
        for j in range(i):
            if array[j] > array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
