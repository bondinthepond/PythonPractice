class ListsPractice:

    list1 = ['physics', 'chemistry', 1997, 2000]
    for i in list1:
        print i
#prints each element in the list

    list2 = [1,2,3,4,5,6]
    print list2
#prints entire list

    list3 = ['a', 'b', 'c', 'd','e']

    print len(list3)    #prints length of the list
    print list3[2:4]    #print from index x to y
    print list3[6:10]   #if index is invalid, does not throw error, displays empty list


    list3[2] = 'C'  #updating the list
    print list3

    del list3[2]  #to delete element at index
    print list3

#   del list3[6]  #list assignment index out of range, if index provided is >max element
#   print list3

    print list2 + list3  #concatenating 2 lists

    print list1+list2+list3  #concatenation 3 lists

    print list3[0]*4  #repetition

    print 3 in list2  #to check membership, returns true if true

    print 3 in list3  #returns false if not ture

    print type(len(list3))  # type method return the type of the parameter passed

    print list3[-1]  # to print the last element of an array

    for index in range(len(list3)): #alternative way to iterate through list
        print 'index',index
        print "value present in list",list3[index]

    list4 = []

    list4.append(10)
    list4.append(20)

    print list4

    print list4.pop(0)

    print list4
    list4.__delitem__(0)

    print list4