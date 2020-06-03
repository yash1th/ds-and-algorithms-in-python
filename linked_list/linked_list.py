class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def insert_after_node(self, previous_node, data):
        if not previous_node:
            print('previous node does not exist')
            return
        
        new_node = Node(data)
        new_node.next = previous_node.next
        previous_node.next = new_node
    
    def delete_node(self, key):
        cur_node = self.head
        # if the node that is to be deleted is head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return
        
        # if the node that is to be deleted is not head
        prev_node = None
        while cur_node and cur_node.data != key:
            prev_node = cur_node
            cur_node = cur_node.next
        
        # if the current node did not match any keys in the linked list
        if cur_node is None:
            return
        
        # now current node has the value that needs to be deleted
        prev_node.next = cur_node.next
        cur_node = None

    def delete_node_at_position(self, pos):
        cur_node = self.head
        # if the node that is to be deleted is head
        if cur_node and pos == 0:
            self.head = cur_node.next
            cur_node = None
            return
        
        # if the node that is to be deleted is not head
        prev_node = None
        count = 0
        while cur_node and count != pos:
            prev_node = cur_node
            cur_node = cur_node.next
            count += 1
        
        # if the current node did not match any keys in the linked list
        if cur_node is None:
            return
        
        # now current node has the value that needs to be deleted
        prev_node.next = cur_node.next
        cur_node = None

    def get_length(self):
        if self.head is None:
            return 0
        
        length = 1
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
            length += 1
        
        return length
    
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
    
    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return
        
        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next
        
        # if prev_1 is not head (not None)
        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2
        
        # if prev_2 is not head (not None)
        if prev_2:
            prev_2.next = curr_1
        else:    
            self.head = curr_1
        
        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    # reversing a linked list iteratively
    def reverse_iterative(self):
        previous_node = None
        current_node = self.head
        while current_node: # as long as current node is not null
            temp_node = current_node.next # copy the next into into a temporary node
            current_node.next = previous_node # change the arrow mark, meaning make the next of current node as previous node
            previous_node = current_node # move the pointer of previous node to current node
            current_node = temp_node # copy the temp node to current node
        self.head = previous_node

    # TODO - understand the below recursive function
    def reverse_recursive(self):
        def _reverse_recursive(cur, prev):
            if not cur:
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur 
            cur = nxt 
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)

l = LinkedList()
l.append('A')
l.append('B')
l.append('C')
l.append('D')
l.print_list()
print('\n\n\n')
# l.reverse_iterative()
l.reverse_recursive()
l.print_list()