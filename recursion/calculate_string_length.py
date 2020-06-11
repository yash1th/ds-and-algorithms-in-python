def iterative_approach(s):
    length = 0
    for i in s:
        length += 1
    return length

def using_built_in(s):
    return len(s)

def recursive_approach(s):
    if s == '':
        return 0
    return 1 + recursive_approach(s[1:])

s1 = ''
s2 = 'a'
s3 = ' '
s4 = 'hello world'

print(using_built_in(s1))
print(using_built_in(s2))
print(using_built_in(s3))
print(using_built_in(s4))
print('-----')
print(iterative_approach(s1))
print(iterative_approach(s2))
print(iterative_approach(s3))
print(iterative_approach(s4))
print('-----')
print(recursive_approach(s1))
print(recursive_approach(s2))
print(recursive_approach(s3))
print(recursive_approach(s4))