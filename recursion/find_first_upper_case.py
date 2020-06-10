def iterative_approach(A):
    for i in A:
        if i.isupper():
            return i
    return "no upper case letters in the string"

def recursive_approach(A, idx):
    if A[idx].isupper():
        return A[idx]
    if idx == len(A) - 1:
        return "no upper case letters in the string"
    else:
        return recursive_approach(A, idx + 1)
    
input_str_1 = "lucidProgramming"
input_str_2 = "LucidProgramming"
input_str_3 = "lucidprogramming"

print(iterative_approach(input_str_1))
print(iterative_approach(input_str_2))
print(iterative_approach(input_str_3))

print(recursive_approach(input_str_1, 0))
print(recursive_approach(input_str_2, 0))
print(recursive_approach(input_str_3, 0))