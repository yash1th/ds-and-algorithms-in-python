from stack import Stack

def reverse_string(string):
    s = Stack()
    for i in string:
        s.push(i)
    result = ''
    while not s.is_empty():
        result += s.pop()
    return result

print(reverse_string('Hello World'))
