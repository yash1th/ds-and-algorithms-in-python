class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
    
    def move_tail_to_head(self):
        if not self.head:
            return
        
        p = self.head
        q = self.head
        prev = None

        while q.next:
            prev = q
            q = q.next
        
        prev.next = None
        q.next = self.head
        self.head = q

l = LinkedList()
l.append('A')
l.append('B')
l.append('C')
l.append('D')
l.print_list()
print('\n\n\n')
l.move_tail_to_head()
l.print_list()