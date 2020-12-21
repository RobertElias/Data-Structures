"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

# With an Array
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
#     # returns the length
#     def __len__(self):
#         return (len(self.storage))
#     # adds to the end of storage
#     def enqueue(self, value):
#         self.size += 1
#         self.storage.append(value)
#     # removes and returns first element    
#     def dequeue(self):
#         if self.size > 0:
#             self.size -= 1
#             return self.storage.pop(0)
        
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    def __init__(self, node=None):
        self.length = 0
        self.head = node
        self.tail = node
        
    # returns the length Array
    def __len__(self):
        return self.length
    # adds an item to the back of the queue
    def enqueue(self,value):
        self.length += 1
        new_node = Node(value)
        # add a node if their is something in the queue
        if self.head:
           self.tail.next = new_node
           self.tail = new_node
        # add a node if que is empty
        else:
            self.head = new_node
            self.tail = new_node
    
    def dequeue(self):
        # something in the que
        if self.head:
            # setting tail and head to none
            if self.head == self.tail:
                current_tail = self.tail
                self.length -= 1
                self.head = None
                self.tail = None
                return current_tail.value
            # will make new item the head item
            else:
                self.length -= 1
                current = self.head
                self.head = self.head.next
                return current.value
            
    