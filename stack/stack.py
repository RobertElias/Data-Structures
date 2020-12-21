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
# Stacks using Arrays


# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
# #self.storage = LinkedList()

#     def __len__(self):
#         return (len(self.storage))

# # Adding to the end of the stack using push

#     def push(self, value):
#         self.storage.append(value)
# # Delete using pop

#     def pop(self):
#         if len(self.storage) > 0:
#             return self.storage.pop()
#         return None



# Using Linked List
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self, node=None):
        self.length = 0
        self.head = node
        self.tail = node
# returns the length Array

    def __len__(self):
        return self.length
# add node to the back of the stack/tail

    def push(self, value):
        self.length += 1
        new_node = Node(value)
        # If there is already something in the stack
        if self.head:
           self.tail.next = new_node
           self.tail = new_node
        # If it the first node in the stack
        else:
            self.head = new_node
            self.tail = new_node
# Pull the last item from the stack and returns it

    def pop(self):
        if self.head:
            # For the it is the last node in the stack
            # Sets head and tail to none and return and delete the node
            if self.head == self.tail:
               current_tail = self.tail
               self.length -= 1
               self.head = None
               self.tail = None
               return current_tail.value
            # If there are more nodes in the stack. Return and delete the last node
            else:
                self.length -= 1
                current = self.head
                last = self.tail
                # Goes to the second to last node
                while current.next != last:
                    current = current.next
                # Make that node the tail
                current.next = None
                self.tail = current
                return last.value