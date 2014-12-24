def selectionsort(array):
    for i in xrange(0, len(array)):
        min_n = i
        for j in xrange(i+1, len(array)):
            if array[j] < array[min_n]:
                array[min_n], array[j] = array[j], array[min_n]

    return array
