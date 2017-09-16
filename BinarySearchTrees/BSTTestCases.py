import BSTDefinition


tree = BSTDefinition.BinarySearchTree()
r = BSTDefinition.Node(10)
tree.insertValueIntoBST(r,12)
tree.insertValueIntoBST(r,11)
tree.insertValueIntoBST(r,13)
tree.insertValueIntoBST(r,14)
tree.insertValueIntoBST(r,15)
tree.insertValueIntoBST(r,9)
tree.insertValueIntoBST(r,8)
tree.insertValueIntoBST(r,19)
tree.insertValueIntoBST(r,18)
tree.insertValueIntoBST(r,16)



tree.traverseInLevelOrder(r)



