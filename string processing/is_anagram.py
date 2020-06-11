def solution_1(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    return sorted(s1) == sorted(s2)

def solution_2(s1, s2):
    if len(s1) != len(s2):
        return False

    ht = {}
    for i in s1:
        if i not in ht:
            ht[i] = 1
        else:
            ht[i] += 1
    
    for i in s2:
        if i in ht and ht[i] > 0:
            ht[i] -= 1
        else:
            return False
    return True


s1 = "fairy tales"
s2 = "rail safety"

print(solution_1(s1, s2))
print(solution_2(s1, s2))