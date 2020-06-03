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
    
    def add_after_node(self, key, data):
        new_node = Node(data)
        cur_node = self.head
        while cur_node:
            if cur_node.next is None and cur_node.data == key:
                self.append(data)
                return

            elif cur_node.data == key:
                new_node.prev = cur_node
                new_node.next = cur_node.next
                cur_node.next.prev = new_node
                cur_node.next = new_node
            
            cur_node = cur_node.next

    def add_before_node(self, key, data):
        new_node = Node(data)
        cur_node = self.head
        while cur_node:
            if cur_node.prev is None and cur_node.data == key:
                self.prepend(data)
            elif cur_node.data == key:
                new_node.prev = cur_node.prev
                new_node.next = cur_node
                cur_node.prev.next = new_node
                cur_node.prev = new_node
            
            cur_node = cur_node.next
    
    def delete_node(self, key):
        # cases to consider when the node to be deleted is
        # 1. head and only one element
        # 2. head and multiple elements
        # 3. any element in between head and tail
        # 4. tail element
        
        cur_node = self.head
        while cur_node: # if it is not empty
            if cur_node.data == key and cur_node == self.head:
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
            elif cur_node.data == key:
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
    
    def reverse(self):
        if self.head:
            cur_node = self.head
            if cur_node.next is None:
                return # cur_node
            else:
                while cur_node:                    
                    nxt = cur_node.next
                    prv = cur_node.prev
                    cur_node.prev = nxt
                    cur_node.next = prv

                    if cur_node.prev is None:
                        self.head = cur_node
                        return
                    cur_node = nxt
        else:
            return

dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.print_list()
print('-----------')
dllist.reverse()
dllist.print_list()
print('-----------')