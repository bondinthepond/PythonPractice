def nextGreatest(arr):
    size = len(arr)

    # Initialize the next greatest element
    max_from_right = arr[size - 1]

    # The next greatest element for the rightmost element
    # is always -1
    arr[size - 1] = -1

    # Replace all other elements with the next greatest
    for i in range(size - 2, -1, -1):

        # Store the current element (needed later for updating
        # the next greatest element)
        temp = arr[i]

        # Replace current element with the next greatest
        arr[i] = max_from_right

        # Update the greatest element, if needed
        if max_from_right < temp:
            max_from_right = temp

    print arr

array1 = [10,9,8,7,6,5,4,3,2]

nextGreatest(array1)