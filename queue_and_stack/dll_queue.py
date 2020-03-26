import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList, ListNode


class Queue:
    def __init__(self):
        self.size = 0
        self.dll = None

        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def enqueue(self, value):
        # if there is no items in list
        # create dll
        if self.size == 0:
            self.dll = DoublyLinkedList(ListNode(value))
        
        else:
            self.dll.add_to_tail(value)
        
        self.size += 1

    def dequeue(self):
        # if list is empty
        if self.size == 0:
            return None
        
        # if list is not empty
        else:
            value = self.dll.head.value
            self.dll.remove_from_head()
            self.size -= 1
            return value

    def len(self):
        return self.size

