"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.level = 0

    # Insert the given value into the tree
    def insert(self, value):
        # go left if valye is less than
        if value >= self.value:
            if self.right:
                #if value is empty
                self.right.insert(value)
            else: #less than node put it left
                self.right = BSTNode(value)
                self.right.level = self.level + 1
        
        else:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
                self.left.level = self.level + 1
                   
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #will compare target against self.value
        if target == self.value:
            #return true if targets match
            return True
        
        if target < self.value:
            #will go left if BST node
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            # will go right if BST node
            if not self.right:
                return False
            return self.right.contains(target)
        

    # Return the maximum value found in the tree
    def get_max(self):
        if self is not None:
            
            current_max = self
            while current_max.right is not None:
                current_max = current_max.right
            return current_max.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        
        if node.left:
            node.left.in_order_print(node.left)
        #print(node.value)
        if node.right:
            node.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # No node
       if node == None:
            return
       queue = []
        # Appends itself
       queue.append(node)
       while(len(queue) > 0):
           print(queue[0].value)
           current = queue.pop(0)
           if current.left != None:
               queue.append(current.left)
           if current.right != None:
               queue.append(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        print(node.value)
        if node.right:
            node.right.dft_print(node.right)
        if node.left:
            node.left.dft_print(node.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
