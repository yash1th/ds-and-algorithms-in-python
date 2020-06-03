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
    
    def prepend(self, data):
        new_node = Node(data)

        # if the cll is empty
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        
        # if the cll is not empty
        cur_node = self.head
        while cur_node.next != self.head:
            cur_node = cur_node.next
        
        new_node.next = cur_node.next
        self.head = new_node
        cur_node.next = self.head
    
    def remove_node(self, key):
        # if the cll is not empty
        if self.head:
            # if the head node is the key to remove
            if self.head.data == key:
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
                while cur_node.data != key:
                    prev_node = cur_node
                    cur_node = cur_node.next
                prev_node.next = cur_node.next
                cur_node = None
        else:
            return
    
    def split_list(self):
        length = self.get_length()
        if length == 0:
            return None
        if length == 1:
            return self.head

        mid = length // 2
        count = 0
        cur_node = self.head
        prev_node = None

        while cur_node and count < mid:
            count += 1
            prev_node = cur_node
            cur_node = cur_node.next
            
        # attaching previous node to head
        prev_node.next = self.head
        
        cll = CircularLinkedList()
        while cur_node.next != self.head:
            cll.append(cur_node.data)
            cur_node = cur_node.next
        cll.append(cur_node.data)
        
        cll.print_list()

        # return cll


cllist = CircularLinkedList()
cllist.append("A")
cllist.append("B")
cllist.append("C")
cllist.append("D")
cllist.append("E")
cllist.append("F")

cllist.split_list()
print('----\n\n\n\n----')
cllist.print_list()

# ll2.print_list()

# l = CircularLinkedList()
# l.append('A')
# l.append('B')
# l.prepend('C')
# l.prepend('D')
# l.prepend('E')
# l.print_list()
# print('\n\n\n')
# l.remove_node('E')
# l.print_list()
# print('\n\n\n')
# l.remove_node('B')
# print('\n\n\n')
# l.print_list()
# l.remove_node('C')
# print('\n\n\n')
# l.print_list()
# print(l.get_length())

# cllist = CircularLinkedList()
# cllist.append("A")
# cllist.append("B")
# cllist.append("C")
# cllist.append("D")

# cllist.remove_node("A")
# cllist.remove_node("C")
# cllist.print_list()