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
    
    def is_palindrome_using_string(self):
        result = ''
        cur = self.head
        while cur:
            result += cur.data
            cur = cur.next
        
        return result == result[::-1]
    
    def is_palindrome_using_stack(self):
        result = []
        cur = self.head
        while cur:
            result.append(cur.data)
            cur = cur.next
        p = self.head
        while p:
            if p.data != result.pop():
                return False
            else:
                p = p.next
        return True
    
    def is_palindrome_using_two_pointers(self):
        if not self.head:
            return True
        
        p = self.head
        q = self.head
        prev = []

        i = 0
        while q:
            prev.append(q.data)
            q = q.next
            i += 1
        
        q = prev[-1]

        count = 1

        while count <= i//2 + 1:
            if prev[-count] != p.data:
                return False
            p = p.next
            count += 1
        
        return True