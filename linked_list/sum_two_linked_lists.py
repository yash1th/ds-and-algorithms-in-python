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
    
    def sum_two_linked_lists(self, llist):
        carry = 0
        i = self.head
        j = llist.head
        result = LinkedList()

        while i or j:
            if not i:
                p = 0
            else:
                p = i.data
            if not j:
                q = 0
            else:
                q = j.data

            total = p + q + carry
            if total >= 10:
                carry = 1
                result.append(total % 10)
            else:
                carry = 0
                result.append(total)

            if i:
                i = i.next
            if j:
                j = j.next

        return result

l1 = LinkedList()
l1.append(5)
l1.append(6)
l1.append(3)

l2 = LinkedList()
l2.append(8)
l2.append(4)
l2.append(2)

l3 = l1.sum_two_linked_lists(l2)
l3.print_list()