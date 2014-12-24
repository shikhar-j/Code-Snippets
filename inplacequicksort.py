def quicksort(array):
    inplacesort(array, 0, len(array) - 1)

def inplacesort(array, left, right):
    if len(array) < 2:
        return array

    pivot = array[(left + right) / 2]

    l = left
    r = right
    while l <= r:
        while array[l] < pivot:
            l += 1

        while array[r] > pivot:
            r -= 1

        if l <= r:
            array[l], array[r] = array[r], array[l]
            l += 1
            r -= 1

    if left < r:
        inplacesort(array, left, r)

    if right > l:
        inplacesort(array, l, right)

    return array

