class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def get_length(self):
        length = 0
        cur_node = self.head
        while cur_node:
            length += 1
            cur_node = cur_node.next
            if cur_node == self.head:
                break
        return length

    def append(self, data):
        new_node = Node(data)

        # if the cll is empty
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        
        # if the cll is not empty
        cur_node = self.head
        while cur_node.next != self.head:
            cur_node = cur_node.next
        
        cur_node.next = new_node
        new_node.next = self.head
    
    def print_list(self):
        cur_node = self.head

        while cur_node:
            print(cur_node.data)
            if cur_node.next == self.head:
                break
            cur_node = cur_node.next
    
    def remove_node(self, node):
        # if the cll is not empty
        if self.head:
            # if the head node is the key to remove
            if self.head== node:
                cur_node = self.head
                while cur_node.next != self.head:
                    cur_node = cur_node.next
                # if the cll has only one element
                if self.head == self.head.next:
                    self.head = None
                else:
                    cur_node.next = self.head.next
                    self.head = cur_node.next
            else:
                cur_node = self.head
                prev_node = None
                while cur_node != node:
                    prev_node = cur_node
                    cur_node = cur_node.next
                prev_node.next = cur_node.next
                cur_node = None
        else:
            return
    
    def josephus_circle(self, step):
        cur_node = self.head
        
        while self.get_length() > 1:
            count = 1
            
            while count != step:
                cur_node = cur_node.next
                count += 1
            print('Kill - ', cur_node.data)
            self.remove_node(cur_node)
            cur_node = cur_node.next

cllist = CircularLinkedList()
cllist.append(1)
cllist.append(2)
cllist.append(3)
cllist.append(4)


cllist.josephus_circle(2)
cllist.print_list()