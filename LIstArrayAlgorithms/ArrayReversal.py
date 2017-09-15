array1 = ['a','b','c','d','e','f','g','h','i','j']

def reverseArray(x):

    for i in range(len(x)/2):
        temp = x[i]
        x[i] = x[len(x) -1 -i]
        x[len(x) -1 -i] = temp

    print x

reverseArray(array1)

array1.reverse()    #return none, but reverses in place, need to print again
print array1

print array1[::-1]  #another trick, but takes up more memory

for element in reversed(array1):  #another trick, using reversed method, reversed method expects an object which is a sequence
    print element

