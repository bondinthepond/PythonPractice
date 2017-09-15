array1 = ['a','b','c','d','e','f','g','h','i','j']

def rotateArrayOnce(list):

    list = list[1:]+list[:1]

    print list

def rotateArrayByN(list, n):

    list = list[n:] + list[:n]

    print list

rotateArrayOnce(array1)

rotateArrayByN(array1, 5)

