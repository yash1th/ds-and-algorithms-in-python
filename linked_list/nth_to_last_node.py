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
    
    def get_length(self):
        cur_node = self.head
        length = 0
        while cur_node:
            length += 1
            cur_node = cur_node.next
        return length
    
    def print_nth_from_last_node(self, n):
        length = self.get_length()
        cur_node = self.head
        while length != n:
            cur_node = cur_node.next
            length -= 1
        return cur_node.data

    # below solution uses two pointers
    def print_nth_from_last(self, n):
        p = self.head
        q = self.head

        count = 0
        # q will move moved ahead +n distance from p
        while q:
            count += 1
            if(count>=n):
                break
            q = q.next
            
        if not q:
            print(str(n) + " is greater than the number of nodes in list.")
            return

        # then both p and q are moved simultaneously until q reaches none
        while p and q.next:
            p = p.next
            q = q.next
        return p.data

l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.print_list()
print(l.print_nth_from_last_node(2))