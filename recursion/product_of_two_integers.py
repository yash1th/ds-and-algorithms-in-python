def built_in(x, y):
    return x * y

def iterative_approach(x, y):
    result = 0
    while y:
        result += x
        y -= 1
    return result

def recursive_approach(x, y):
    # to decrease the recursive calls and avoiding below recursion error
    # RecursionError: maximum recursion depth exceeded
    if x < y:
        recursive_approach(y, x)
    if y == 0:
        return 0
    return x + recursive_approach(x, y - 1)



x = 15
y = 12

print(built_in(x, y))
print(iterative_approach(x, y))
print(recursive_approach(x, y))