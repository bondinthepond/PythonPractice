def reverse(string):
    result = ''

    #range(start, stop, step), step = -1, implies reverse iteration
    for i in range(len(string), 0, -1):
        result += string[i - 1]
    print result

    print string[::-1]

input = 'aditya'
reverse(input)