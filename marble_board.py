"""
You have a n*n board (grid) with a few marbles lying around in some grids.
A new marble can be placed at location (X,Y) only if there is at least one marble in
north, east, west and south of the marble. They need not be present immediatly next to 
(X,Y). Find all possible positions where a new marble can be placed.

Input:
    line 1 will have two number - the size of matrix and number of existing marbles (n k)
    next k number of lines will have coordinates for each marble

eg:
    6 7
    0 1
    1 0
    1 2
    1 5
    4 2
    5 1
    4 0

PS: This is a terrible solution but it works
"""

line1 = raw_input("n k").split()
n, k = line1

n = int(n)
k = int(k)

#Matrix
m = [[False for i in xrange(n)] for i in xrange(n)]
for i in xrange(0, n):
    for j in xrange(0, n):
        m[i][j] = False
    
for i in xrange(0, k):
    x,y = raw_input("location for marble {0}".format(i)).split()
    x = int(x)
    y = int(y)
    m[x][y] = True

def is_valid(m, i, j, n):
    # No marble can possibly be present on at least two directions
    # from such postions (i.e. each corner)
    if i == 0 or j == 0 or i == n or j == n:
        return False

    east = False
    west = False
    north = False
    south = False

    x = i+1
    while x < n:
        if m[x][j]:
            east = True
            break
        else:
            x += 1
    
    x = i - 1
    while x >= 0:
        if m[x][j]:
            west = True
            break
        else:
            x -= 1

    x = j+1
    while x < n:
        if m[i][x]:
            north = True
            break
        else:
            x += 1
    
    x = j - 1
    while x >= 0:
        if m[i][x]:
            south = True
            break
        else:
            x -= 1

    if east and west and north and south:
        return True
    
    return False

for i in xrange(0, n):
    for j in xrange(0, n):
        east = False
        west = False
        north = False
        south = False
        
        if is_valid(m, i, j, n):
            print "Valid: {0} {1}".format(i,j)
        else:
            continue
