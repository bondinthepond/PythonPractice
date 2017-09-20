numberOfElements = int(raw_input())

inputString = raw_input()
listOfElements = inputString.split()

for str in listOfElements:
    str = int(str)


numberOfQueries = int(raw_input())

listOfQueries = []*numberOfQueries
for i in range(0, numberOfQueries):
        tempList = raw_input().split()
        if len(tempList) == 2:
            listOfQueries.append(int(tempList[0]))
            listOfQueries.append(int(tempList[1]))


n = len(listOfQueries)

def numberOfDistinctElements(listOfElements, start, end):
    tempList = listOfElements[start-1:end]
    distinctSet = set(tempList)

    result = len(distinctSet)
    print result


for q in range(0, n, 2):
    start = listOfQueries[q]
    end = listOfQueries[q+1]
    numberOfDistinctElements(listOfElements, start, end)



