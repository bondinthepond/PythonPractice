
def quickSort(list, low, high):
    print 'quick sort between', low , high
    pivot = list[low + (high - low)/2]
    print pivot

    pointer1 = low
    pointer2 = high

    while pointer1 <= pointer2:
        while list[pointer1] < pivot:
            pointer1+=1

        while list[pointer2] > pivot:
            pointer2-=1

        if pointer1 <= pointer2:
            var = list[pointer1]
            list[pointer1] = list[pointer2]
            list[pointer2] = var
            pointer1+=1
            pointer2-=1
        print "after swap",list
        if pointer1 > low:
            quickSort(list, pointer1, high)

        if pointer2 < high:
            quickSort(list, low, pointer2)

    print list

input_list =[7,1,2,3,4,0,9,3]

quickSort(input_list, 0, len(input_list)-1)