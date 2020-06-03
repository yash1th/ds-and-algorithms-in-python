# my solution
def is_circular_linked_list(self, input_list):
    if not input_list.head:
        return True
    
    if not input_list.head.next:
        return False

    cur_node = input_list.head
    
    while cur_node:
        if cur_node.next == input_list.head:
            return True
        cur_node = cur_node.next
    return False

# educative solution
def is_circular_linked_list(self, input_list):
  cur = input_list.head
  while cur.next:
    cur = cur.next
    if cur.next == input_list.head:
      return True
  return False