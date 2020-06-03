from stack import Stack

def decimal_to_binary(dec_num):
    s = Stack()
    while dec_num:
        s.push(str(dec_num%2))
        dec_num //= 2

    result = ''
    while not s.is_empty():
        result += s.pop()
    return result

print(decimal_to_binary(16))
