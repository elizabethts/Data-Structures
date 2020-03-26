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
    def add_to_head(self, value):
        node = ListNode(value)
        cur_head = self.head
        self.head = node

        self.length += 1
        if cur_head:
            cur_head.prev = self.head
            self.head.next = cur_head
        else:
            self.tail = node

        


    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value


    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        node = ListNode(value)
        cur_tail = self.tail

        self.tail = node
        # if list is not empty
        if cur_tail:
            
            cur_tail.next = self.tail
            self.tail.prev = cur_tail

        else:
            self.head = self.tail
        
        self.length += 1

        


    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):

        value = self.tail.value
        self.delete(self.tail)
        return value

            
        

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        node_next = node.next
        node_prev = node.prev
        cur_head = self.head

        # if node is the head
        if node_prev == None:
            pass


        # if node is the tail
        elif node_next == None:
            self.tail = node_prev
            self.head = node
            cur_head.prev = self.head
            self.head.next = cur_head


        # else node in middle
        else:
            self.head = node
            cur_head.prev = self.head
            self.head.next = cur_head
            node.delete



    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node is self.tail:
            return
        value = node.value
        self.delete(node)
        self.add_to_tail(value)



    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        is_node = isinstance(node,ListNode)
        if is_node:
            cur = node
            cur_next = cur.next
            cur_prev = cur.prev

            # if list is 1 item long
            if self.length < 2:
                self.head = None
                self.tail = None
            
            else:
                # if head
                if cur_prev == None:
                    self.head = self.head.next
                    node.delete()
                    
                # if tail
                elif cur_next == None:
                    self.tail = self.tail.prev
                    node.delete()

                # else
                else:
                    node.delete()

            self.length -= 1

        
    """Returns the highest value currently in the list"""
    def get_max(self):
        is_node = isinstance(self,DoublyLinkedList)
        if is_node:
            max_count = 0
            cur = self.head
            # list has no items
            if cur == None:
                return max_count

            # list is 1 item
            elif cur.next == None:
                max_count = cur.value
                
            else:
                max_count = cur.value
                while cur.next:
                    value = cur.next.value
                    if value > max_count:
                        max_count = value
                    cur = cur.next
        
        else:
            max_count = self.value
        return max_count
