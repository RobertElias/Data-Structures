"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly."""
    # will create a node at the front

    def add_to_head(self, value):
        self.length += 1
        if self.head == None and self.tail == None:
            newNode = ListNode(value)
            self.head = newNode
            self.tail = newNode
        else:
            # make a new node with next assigning value to head
            newNode = ListNode(value, None, self.head)
            self.head = newNode
            newNode.next.prev = newNode

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    # removes the node

    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        self.length += 1

        if self.head == None and self.tail == None:
            newNode = ListNode(value)
            self.tail = newNode
            self.head = newNode

        else:
            newNode = ListNode(value, self.tail, None)
            self.tail = newNode
            newNode.prev.next = newNode

    """Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    # dletes last node & returns the value

    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the
    List and inserts it as the new head node of the List."""
    # deletes node from current location then adds to the front list

    def move_to_front(self, node):
        value = node.value
        self.delete(node)
        self.add_to_head(value)
        

    """Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List."""
    # deletes node from current location then adds to the end of list

    def move_to_end(self, node):
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        self.length -= 1
        # set head and tail to none
        if self.head == self.tail:
            self.head.delete()
            self.head = None
            self.tail = None
        # new node if first node
        elif self.head == node:
             self.head = node.next
             self.head.prev = None
             node.delete()
        # new tail if last node
        elif self.tail == node:
            self.tail = node.prev
            self.tail.next = None
            node.delete()
        # connect nodes before and after the node to each other and deletes it
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.delete()

    """Returns the highest value currently in the list"""

    def get_max(self):
        highest = self.head.value
        current = self.head

        while True:
            if current.value > highest:
                highest = current.value
            if current.next == None:
                break

            current = current.next

        return highest

 
