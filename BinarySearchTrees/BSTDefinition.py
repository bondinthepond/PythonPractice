class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.height = 0

    def __sizeof__(self):
        return self.size

    def sizeOfTree(self):
        return self.size

    def heightOfTree(self):
        return self.height


    def insertValueIntoBST(self, root, value):

        node = Node(value)

        if root is None:
            print 'root is empty'
            root = node
            print 'inserted', value, 'at root'
        else:
            if root.data > value:
                if root.left_child is None:
                    root.left_child = Node(value)
                    print 'inserted', value, 'at left'
                elif root.left_child:
                    self.insertValueIntoBST(root.left_child, value)
            elif root.data< value:
                if root.right_child is None:
                    root.right_child = Node(value)
                    print 'inserted', value, 'at right'
                elif root.right_child:
                    self.insertValueIntoBST(root.right_child, value)




    def traverseInLevelOrder(self, root):

        if root is None:
            return

        queueOfNodes = []

        queueOfNodes.append(root)

        while len(queueOfNodes) > 0:
            print queueOfNodes[0].data
            node = queueOfNodes.pop(0)

            if node.left_child is not None:
                queueOfNodes.append(node.left_child)

                # Enqueue right child
            if node.right_child is not None:
                queueOfNodes.append(node.right_child)


    def traverseInSpiralOrder(self, root):

        if root is None:
            return

        stackOfNodes = []

        stackOfNodes.append(root)







