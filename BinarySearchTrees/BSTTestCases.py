import BSTDefinition


tree = BSTDefinition.BinarySearchTree()
r = BSTDefinition.Node(10)
tree.insertValueIntoBST(r,12)
tree.insertValueIntoBST(r,11)
tree.insertValueIntoBST(r,13)
tree.insertValueIntoBST(r,8)
tree.insertValueIntoBST(r,9)
tree.insertValueIntoBST(r,7)
tree.insertValueIntoBST(r,6)










tree.traverseInLevelOrder(r)

print 'inorder traversal'
tree.traverse_In_InOrder(r)

print 'post order traversal'
tree.traverse_In_PostOrder(r)

print 'height'
print tree.heightOfTree(r)

for i in range(1,10):
    print 'level', i
    tree.printAtGivenLevel(r, i)


print 'sprial order traversal'
tree.printInSpiralLevelOrder(r)

tree.lowest_common_ancestor(r, 7, 6)


tree.printNodesAtKDistance(r, 2)

key = 0
dictOfColumns = {key : []}
tree.columnWiseTraversal(key, r, dictOfColumns)