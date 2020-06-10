"""
    Find First Entry in List with Duplicates
"""
def by_linear_search(A, target):
    for i, v in enumerate(A):
        if v == target:
            return i
    return None

def by_binary_search(A, target):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high) // 2
        if A[mid] < target:
            low = mid + 1
        elif A[mid] > target:
            high = mid - 1
        else:
            if mid - 1 < 0:
                return mid
            if A[mid-1] != target:
                return mid
            high = mid - 1
            

A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
target = 108

print(by_linear_search(A, target))
print(by_binary_search(A, target))