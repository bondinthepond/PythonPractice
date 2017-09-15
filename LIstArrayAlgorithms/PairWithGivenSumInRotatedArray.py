def pairInSortedRotated(list, sum):

    length = len(list)
    pivot = findPivotOfSortedArray(list, 0, length-1)

    print 'pivot :' ,pivot
    low = (pivot + 1)%length
    high = pivot

    while low != high :
        if list[low] + list[high] == sum :
            return True
        if list[low] + list[high] < sum :
            low = (low+1)%length
            print 'low :' ,low
        else :
            high = (length - 1 + high)%length
            print 'high :',high

    return False


def findPivotOfSortedArray(list, low, high):

    print list


    mid = (low + high)/2

    if low == high :
        return mid
    if mid < high and list[mid] > list[mid+1]:
        return mid
    if mid > low and list[mid] < list[mid-1]:
        return mid-1
    if list[low] >= list[mid]:
        return findPivotOfSortedArray(list, low, mid-1)
    return findPivotOfSortedArray(list, mid+1, high)

array1 = [2,3,4,5,6,7,8,9,10,0]

print pairInSortedRotated(array1, 16)
