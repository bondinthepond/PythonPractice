class Node:
    def __init__(self, data):                       #constructor, fisrt argument to each constructor is self
        self.data = data  # Assign data
        self.next = None  # Initialize next as null

class LinkedLists:
    def __init__(self):
        self.head = None

    def push(self, new_data):

        newNode = Node(new_data)
        newNode.next = self.head
        self.head = newNode



