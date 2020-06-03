"""
Implement stack data structure
"""

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

# running the above stack data structure
# s = Stack()
# print(s.get_stack())
# s.push(1)
# s.push(2)
# print(s.et_stack())
# s.push('A')
# print(s.get_stack())
# print(s.peek())
# s.pop()
# print(s.get_stack())
