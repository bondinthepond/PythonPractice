first_string = 'python'

#first_string[2] = 'T'     #error, Strings in Python are immutable


second_string = " ruby"     #Both Single quotes and double quotes can be used in creation
thrid_string = ''' java 
rocks'''

print first_string
print second_string
print thrid_string

print first_string+second_string+thrid_string

print "He says \"I am batman \" " #By using double quotes, escape characters will have to be used to display quotes

print 'He says "I am superman"'  #a combination of quotes can be used to display quotes

#Python has no char type, chars are string with length 1

print first_string[1:5]

#substring/slice - if x and y are equal no response, but no error
#           if x > y, no response, but no error

print 'h' in first_string    #to check presence

print "a" not in first_string  #to check absence

print first_string*2

#String formatting operator

print 'my name is %s and age is %d' % ('aditya', 28)

#String built In methods

print first_string.capitalize()   #makes the first letter as caps
print first_string.center(10, 'x')  # gives out put as xxpythonxx - length 10
print thrid_string.count('a')       #gives how many times, he paramets occurs through the string/ sub string

print thrid_string.find('v')        #return index of first occurance in the string

print thrid_string.isdigit()   #many boolean methods, isalpha(, isalnum(), isupper(), islower()

print 'ADITYA'.lower()

print 'aditya'.upper()

print min('adityaADITYA')
print max('adityaADITYA')

print 'adityaADITYA'.swapcase()