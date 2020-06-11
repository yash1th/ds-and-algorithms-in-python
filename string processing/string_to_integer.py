def string_to_integer(input_str):
    total = 0
    if input_str[0] == '-':
        start = 1
        exp = len(input_str) - 2
    else:
        start = 0
        exp = len(input_str) - 1
    for i in input_str[start:]:
        total += int(i) * (10 ** exp)
        exp -= 1
    return -total if start else total

print(string_to_integer('0'))
print(string_to_integer('-123'))
print(string_to_integer('89'))