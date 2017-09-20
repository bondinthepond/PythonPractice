import sys

sys.setrecursionlimit(10000)

def mergeSortArray(list, low, high):
    if low < high:

        mid = (low + high)/2

        mergeSortArray(list, low, mid)
        mergeSortArray(list, mid+1, high)

        merge(list, low, mid, high)


def merge(list, low, mid, high):
    print 'merge', low, mid, high

    n1 = mid - low + 1   #becuase array will be from low to mid
    n2 = high - mid      #because array will be from mid+1 to high

    l_list = [0] * n1
    r_list = [0] * n2


    for i in range(0, n1):
        l_list[i] = list[int(low) + i]

    print l_list

    for j in range(0, n2):
        r_list[j] = list[int(mid) + 1 + j]

    print r_list

    pointer1 = 0
    pointer2 = 0
    pointer3 = low

    while pointer1 < n1 and pointer2 < n2:
        print 'pointer1' , pointer1 , 'n1', n1 , 'pointer2', pointer2, 'n2', n2
        if l_list[pointer1] <= r_list[pointer2]:
            list[pointer3] = l_list[pointer1]
            print list[pointer3], pointer3
            pointer1 += 1
        else:
            list[pointer3] = r_list[pointer2]
            pointer2 += 1
        pointer3 += 1

    # if pointer1 hasn't reached max, and items are still remaining
    while pointer1 < n1:
        list[pointer3] = l_list[pointer1]
        pointer1 += 1
        pointer3 += 1

    while pointer2 < n2:
        list[pointer3] = r_list[pointer2]
        pointer1 += 1
        pointer2 += 1

    print list




mergeSortArray(input_list, 0, len(input_list) - 1)