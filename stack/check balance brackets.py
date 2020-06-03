from stack import Stack

def is_match(a, b):
    if a == '(' and b == ')':
        return True
    elif a == '[' and b == ']':
        return True
    elif a == '{' and b == '}':
        return True
    else:
        return False

def is_brackets_balanced(brackets_string):
    s = Stack()
    for i in brackets_string:
        if i in '{[(':
            s.push(i)
        else:
            if not s.is_empty():
                open_paran = s.pop()
                if not is_match(open_paran, i):
                    return False
            else:
                return False
    return s.is_empty()

print(is_brackets_balanced('{([])}}'))
print(is_brackets_balanced('([{}])'))

print("String : (((({})))) Balanced or not?")
print(is_brackets_balanced("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(is_brackets_balanced("[][]]]"))

print("String : [][] Balanced or not?")
print(is_brackets_balanced("[][]"))

print("String : [ Balanced or not?")
print(is_brackets_balanced("["))


