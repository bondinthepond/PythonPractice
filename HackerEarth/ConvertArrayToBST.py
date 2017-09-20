import sys

sys.setrecursionlimit(10000)

class Node:

    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None

class BST:

    def __init__(self):
        self.root = None

    def insertRoot(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
        return self.root


    def insertData(self, root, data):

        node = Node(data)

        if data > root.data:
            if root.right_child is None:
                root.right_child = node
            elif root.right_child:
                self.insertData(root.right_child, data)

        if data <= root.data:
            if root.left_child is None:
                root.left_child = node
            elif root.left_child:
                self.insertData(root.left_child, data)



    def heightOfBinaryTree(self, root):

        if root is None:
            return -1

        if root.right_child is None and root.left_child is None:
            return 1

        leftHeight = self.heightOfBinaryTree(root.left_child)
        rightHeight =self.heightOfBinaryTree(root.right_child)

        if leftHeight > rightHeight:
            return leftHeight+1
        else:
            return rightHeight+1


   # def findLowestCommonAncestor(self, root, start, end):


 #   def findMaximumBetweenNodes(self, start, end):


    def findPathFromRoot(self, path, root, end):

        path.append(root.data)
        if root is None:
            return -1
        if root.right_child is None and root.left_child is None:
            return path
        if end < root.data:
            self.findPathFromRoot(path, root.left_child, end)
        if end > root.data:
            self.findPathFromRoot(path, root.right_child, end)

        return path

    def findLowestCommonAncestor(self, root, start, end):

        path1 = []
        path2 = []

        path1 = self.findPathFromRoot(path1, root, start)
        path2 = self.findPathFromRoot(path2, root, end)

        i = 0
        while i < len(path1) and  i< len(path2):

            if path1[i] != path2[i]:
                break
            i+=1

        return path1[i-1]

    def findPathFromXToY(self, root, start, end):

        path1 = []
        path2 = []
        path3 = []

        path1 = self.findPathFromRoot(path1, root, start)
        path2 = self.findPathFromRoot(path2, root, end)

        i = 0
        while i < len(path1) and i < len(path2):

            if path1[i] != path2[i]:
                break
            i += 1

        for j in range(len(path1)-1, i-1, -1):
            path3.append(path1[j])
        for k in range(i-1, len(path2)):
            path3.append(path2[k])

        return path3



numberOfElements = int(raw_input())
listOfElements = raw_input().split()

for i in range(0, numberOfElements):
    listOfElements[i] = int(listOfElements[i])



tree = BST()
root = tree.insertRoot(listOfElements[0])
for j in range(1, numberOfElements):
    tree.insertData(root, listOfElements[j])

# path = []
# path = tree.findPathFromRoot(path, root, 3)
# print path
#
# print tree.findLowestCommonAncestor(root, 15 , 16)
#
# path3 = []

xAndY = raw_input().split()

x = int(xAndY[0])
y = int(xAndY[1])


path3 = tree.findPathFromXToY(root, x, y)

print max(path3)


