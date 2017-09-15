
def findpivot(list, low, high):

    if high < low :
        return -1;
    if high == low :
        return low

    mid = (low + high)/2;

    if mid < high and list[mid] > list[mid + 1]:
        return mid;
    if mid > low and list[mid] < list[mid - 1]:
        return (mid - 1);
    if list[low] >= list[mid]:
        return findpivot(list, low, mid - 1);
    return findpivot(list, mid + 1, high);

def binaryserach_array(list, low, high, search_parameter) :

    if high < low :
        return -1

    mid = (low + high) / 2;

    if list[mid] == search_parameter :
        return mid
    if list[mid] < search_parameter :
        return binaryserach_array(list, mid+1, high, search_parameter)
    if list[mid] > search_parameter :
        return binaryserach_array(list, low, mid-1, search_parameter)

def pivoted_binarysearch(list, search_parameter):

    low = 0
    high = len(list)-1
    pivot = findpivot(list,low,high)

    if pivot == -1 :
        return binaryserach_array(list, low, high, search_parameter)
    if list[pivot] == search_parameter :
        return pivot
    if list[0] <= search_parameter :
        return binaryserach_array(list, low, pivot-1, search_parameter)
    return binaryserach_array(list, pivot+1, high, search_parameter)

array1 = ['e','f','g','h','i','j','a','b','c','d']

print pivoted_binarysearch(array1, 'h')