"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

# STACK OF PLATES AT A BUFFET! THE PLATE AT THE BOTTOM OF THE STACK WAS THE FIRST ONE ADDED

# WITH LINKED LIST


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def __len__(self):
        return self.size

    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)

#     def pop(self):
#         return self.storage.pop()

# WITH ARRAY
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)

#     def pop(self):
#         return self.storage.pop()

# class Node:

#     def __init__(self):
#         self.data = None
#         self.next = None

#     def getData(self):
#         return self.data

#     def getNext(self):
#         return self.next

#     def setData(self, newdata):
#         self.data = newdata

#     def setNext(self, newnext):
#         self.next = newnext


# class Stack:

#     def __init__(self):
#         self.head = None

#     def __len__(self):
#         temp = Node()
#         temp = self.getData()
#         return len(self.head)

#     def push(self, data):

#         temp = Node()
#         temp.setData(data)
#         temp.setNext(self.head)
#         self.head = temp

#     def pop(self):

#         temp = Node()
#         temp = self.getData()
#         self.head = self.head.getNext()
#         return temp
