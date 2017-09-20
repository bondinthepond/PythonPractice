numberOfCases = int(raw_input())

listOfCases = []
listOfNsAdnKs = []
for i in range(0, numberOfCases):
    nAndkString = raw_input().split()

    for each in range(0, 2):
        nAndkString[each] = int(nAndkString[each])

    listOfNsAdnKs.append(nAndkString)

    listOfElements = raw_input().split()
    length = len(listOfElements)
    for each1 in range(0, length):
        listOfElements[each1] = int(listOfElements[each1])
    listOfCases.append(listOfElements)

for case in range(0, numberOfCases):
    listOfElement = listOfCases[case]
    K = listOfNsAdnKs[case][1]
    result = K - min(listOfElement)
    if result < 0:
        result = 0
    print result
