vowels = set('aeiou')

def iterative_approach(s):
    cnt = 0
    for i in s:
        if i.isalpha() and i.lower() not in vowels:
            cnt += 1
    return cnt

def recursive_approach(s):
    if s == '':
        return 0
    if s[0].isalpha() and s[0].lower() not in vowels:
        return 1 + recursive_approach(s[1:])
    return recursive_approach(s[1:])

s1 = "abc de"
s2 = "LuCiDPrograMMiNG"

print(iterative_approach(s1))
print(iterative_approach(s2))
print('----')
print(recursive_approach(s1))
print(recursive_approach(s2))