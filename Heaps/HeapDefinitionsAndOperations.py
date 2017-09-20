class Heaps:

    def __init__(self):
        self.listofelements = []
        self.size = len(self.listofelements)

    def heapifyfromend(self, list, currentIndex):
        parentIndex = (currentIndex - 1) / 2

        while (parentIndex >= 0):

            if (list[currentIndex] > list[parentIndex]):
                list[currentIndex], list[parentIndex] = list[parentIndex], list[currentIndex]

            currentIndex = parentIndex
            parentIndex = (parentIndex-1)/2

    def heapifyfromtop(self, list, currentIndex):
        parentIndex = currentIndex
        childIndexLeft = parentIndex*2 + 1
        childIndexRight = parentIndex*2 + 2

        if childIndexLeft < len(list) and list[currentIndex] < list[childIndexLeft]:
            parentIndex = childIndexLeft

        if childIndexRight < len(list) and list[parentIndex] < list[childIndexRight]:
            parentIndex = childIndexRight

        if parentIndex != currentIndex:
            list[parentIndex], list[currentIndex] = list[currentIndex], list[parentIndex]

            self.heapifyfromtop(list, parentIndex)

    def insertElement(self, data):

        if len(self.listofelements) == 0:
            self.listofelements.append(data)
            return

        if len(self.listofelements) > 0:
            self.listofelements.append(data)
            currentIndex = len(self.listofelements) - 1
            self.heapifyfromend(self.listofelements, currentIndex)

        print self.listofelements


    def deleteMaximum(self):

        self.listofelements[0], self.listofelements[-1] = self.listofelements[-1], self.listofelements[0]

        self.listofelements.__delitem__(-1)

        currentIndex = 0
        self.heapifyfromtop(self.listofelements, currentIndex)

        print self.listofelements


