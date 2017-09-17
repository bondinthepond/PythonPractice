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

    def heightOfTree(self, root):
        if root is None:
            return 0
        else:
            left_height = self.heightOfTree(root.left_child)
            right_height = self.heightOfTree(root.right_child)

        if left_height > right_height:
            return left_height+1
        else:
            return right_height+1


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
            elif root.data < value:
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


    def traverse_In_InOrder(self, root):

    #left, root, right - gives a sorted output

        if root is None:
            return

        if root.left_child:
            self.traverse_In_InOrder (root.left_child)

        print root.data

        if root.right_child:
            self.traverse_In_InOrder(root.right_child)


    def traverse_In_PostOrder(self, root):

    #left, right, root

        if root is None:
            return

        if root.left_child:
            self.traverse_In_PostOrder(root.left_child)

        if root.right_child:
            self.traverse_In_PostOrder(root.right_child)

        print root.data

    def printAtGivenLevel(self, root, level):

        if root is None:
            return

        if level == 1:
            print root.data
        elif level > 1:
            self.printAtGivenLevel(root.left_child, level-1)
            self.printAtGivenLevel(root.right_child, level-1)

    def printInSpiralLevelOrder(self, root):

        if root is None:
            return

        stack1 = []
        stack2 = []

        stack1.append(root)

        while len(stack1) > 0 or len(stack2) > 0:

            while len(stack1) > 0:
                node1 = stack1.pop(-1)
                print node1.data

                if node1.right_child:
                    stack2.append(node1.right_child)

                if node1.left_child:
                    stack2.append(node1.left_child)

            while len(stack2) > 0:
                node2 = stack2.pop(-1)
                print node2.data

                if node2.left_child:
                    stack1.append(node2.left_child)

                if node2.right_child:
                    stack1.append(node2.right_child)


    def lowest_common_ancestor (self, root, val1, val2):
        if root is None:
            return

        if root.data > val1 and root.data > val2:
             return self.lowest_common_ancestor(root.left_child, val1, val2)

        if root.data < val1 and root.data < val2:
             return self.lowest_common_ancestor(root.right_child, val1, val2)

        print 'lca', root.data
        return root

    def printNodesAtKDistance(self,root, k):

        if root is None:
            return
        if k == 0:
            print root.data
        else:
            self.printNodesAtKDistance(root.left_child, k-1)
            self.printNodesAtKDistance(root.right_child, k-1)


    def columnWiseTraversal(self, key, root, dictOfColumns):


        if root is None:
            return
        else:
            if dictOfColumns.has_key(key):
                dictOfColumns[key].append(root.data)
            else :
                dictOfColumns.setdefault(key, [])
                dictOfColumns[key].append(root.data)

        if root.left_child or root.right_child:
            self.columnWiseTraversal(key-1, root.left_child, dictOfColumns)
            self.columnWiseTraversal(key+1, root.right_child, dictOfColumns)

        print dictOfColumns


