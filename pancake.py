def pancakesort(stack, start = 0):
    if start >= len(stack):
        return stack

    curr = start
    max_index = start
    bottom = len(stack) - 1
    while curr < bottom:
        if stack[max_index] < stack[curr+1]:
            max_index = curr + 1
        curr += 1

    stack[max_index:] = stack[:(max_index-1):-1]

    if start > 0 :
        stack[start:] = stack[:start-1:-1]
    else:
        stack[start:] = stack[::-1]

    return pancakesort(stack, start + 1)
