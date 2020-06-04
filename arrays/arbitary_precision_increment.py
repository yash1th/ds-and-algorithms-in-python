A1 = [1, 4, 9]
A2 = [9, 9, 9]

def arbitary_precision_increment_1(A):
    A[-1] += 1
    for i in range(len(A) - 1, 0, -1):
        if A[i] > 9:
            carry = 1
            A[i] = A[i] % 10
            A[i - 1] += carry
        else:
            carry = 0
            A[i] += carry
    
    if A[0] > 9:
        A.insert(0, 1)
        A[1] = A[1] % 10    
    
    return A


def arbitary_precision_increment_2(A):
    A[-1] += 1
    for i in range(len(A) - 1, 0, -1):
        if A[i] != 10: # 148 + 1 = 149
            break
        A[i] = 0
        A[i-1] += 1
    if A[0] == 10:
        A[0] = 1
        A.insert(1, 0) # A.append(0)
    return A


print(arbitary_precision_increment_2(A1))
print(arbitary_precision_increment_2(A2))