def mergesort(array):
    if len(array) < 2:
        return array

    left = mergesort(array[:len(array)/2])
    right = mergesort(array[len(array)/2:])

    return merge(left, right)

def merge(left, right):
    array = []

    l = 0
    r = 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            array.append(left[l])
            l += 1
        else:
            array.append(right[r])
            r += 1

    if l < len(left):
        array.extend(left[l:])

    if r < len(right):
        array.extend(right[r:])
    
    return array

