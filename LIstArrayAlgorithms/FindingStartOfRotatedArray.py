def find_start_of_array (list) :
    #input will a sorted but rotated array

    high = len(list)-1
    low = 0

    mid = (low+ high)/2

    if len(list) == 1 :                #if only 1 element, return 1 or if high == low
        return mid
    if mid < high and list[mid] > list[mid+1]:
        return mid
    if low < mid and list[mid] < list[mid-1]:
        return mid-1;


    if list[low] >= list[mid]:
        return find_start_of_array(list, low, mid-1)
    return find_start_of_array(list, mid+1, high)
