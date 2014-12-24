def selectionsort(array):
    for i in xrange(0, len(array)):
        min_n = i
        for j in xrange(i+1, len(array)):
            if array[j] < array[min_n]:
                insert(array, index, end) 

    return array

def insert(array, index, start):
    while index > start:
        temp = array[index]
        for i in xrange(index, start+1):
            array[i] = array[i-1]

        array[start] = temp


