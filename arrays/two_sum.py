def solution_1(A, target):
    # brute force technique by using two pointers
    result = []
    for i in range(len(A) - 1):
        for j in range(i+1, len(A)):
            if A[i] + A[j] == target:
                result.append((A[i], A[j]))
    return result if result else False

def solution_2(A, target):
    # using dictionary
    d = dict()
    for i in A:
        if i in d:
            print(i, d[i])
            return True
        else:
            d[target - i] = i
    return False


# Time Complexity: O(n)
# Space Complexity: O(1)
def solution_3(A, target):
    # in order for this to work, the list has to be in sorted order
    i = 0
    j = len(A) - 1
    while i < j:
        if A[i] + A[j] == target:
        print(A[i], A[j])
        return True
        elif A[i] + A[j] < target:
        i += 1
        else:
        j -= 1
    return False