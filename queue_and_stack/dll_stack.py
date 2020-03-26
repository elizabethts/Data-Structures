import sys
# sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList, ListNode

class Stack:
    def __init__(self):
        self.size = 0
        self.dll = None
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def push(self, value):
        if self.dll:
            self.dll.add_to_head(value)
        else:
            self.dll = DoublyLinkedList(ListNode(value))

        self.size += 1

    def pop(self):

        if self.dll:
            value = self.dll.head.value
            self.dll.remove_from_head()
            self.size -= 1 
            

        else:
            value = None

        return value

    def len(self):
        return self.size