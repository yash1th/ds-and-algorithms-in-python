class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head: # if dll is empty
            self.head = new_node
        else: # if dll is not empty
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = new_node
            new_node.prev = cur_node
    
    def prepend(self, data):
        new_node = Node(data)
        if not self.head: #if dll is empty
            self.head = new_node
        else: # if dll is not empty
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
    
    def delete_node(self, node):
        # cases to consider when the node to be deleted is
        # 1. head and only one element
        # 2. head and multiple elements
        # 3. any element in between head and tail
        # 4. tail element
        
        cur_node = self.head
        while cur_node: # if it is not empty
            if cur_node == node and cur_node == self.head:
                if cur_node.next is None:
                    cur_node = None
                    self.head = None
                    return
                else: #
                    nxt = self.head.next
                    nxt.prev = None
                    self.head = nxt
                    cur_node = None
                    return
            elif cur_node == node:
                if cur_node.next is None:
                    prev = cur_node.prev
                    prev.next = None
                    cur_node = None
                    return
                else:
                    prv = cur_node.prev
                    nxt = cur_node.next
                    prv.next = nxt
                    nxt.prev = prv
                    cur_node = None
                    prv = None
                    nxt = None
                    return
            cur_node = cur_node.next
        else: # if it is empty
            return
        
    def remove_duplicates(self):
        if self.head:
            dup = set()
            cur_node = self.head
            while cur_node:
                if cur_node.data not in dup:
                    dup.add(cur_node.data)
                    cur_node = cur_node.next
                else:
                    nxt = cur_node.next
                    self.delete_node(cur_node)
                    cur_node = nxt

        else:
            return