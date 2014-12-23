def quicksort(arr):
    if len(arr) < 2:
        return arr

    pivot_index = (len(arr) / 2) - 1
    pivot = arr[pivot_index]
    left = []
    right = []

    for i in xrange(0, len(arr)):
        if arr[i] == pivot:
            continue
        elif arr[i] < pivot:
            left.append(arr[i])
        elif arr[i] > pivot:
            right.append(arr[i])

    left = quicksort(left)
    right = quicksort(right)

    return left + [pivot] + right


