"""
    definition - An array is “cyclically shifted” if it is possible to shift its entries cyclically so that it becomes sorted.
    problem - determine the index of the smallest element of the cyclically shifted array.
"""
def by_brute_force(A):
    sortedA = sorted(A)
    return A.index(sortedA[0])

def by_binary_search(A):
    low = 0
    high = len(A) - 1
    while low < high:
        mid = (low + high) // 2

        if A[mid] <= A[high]:
            # middle element is less than last means
            # second half of array is increasing
            high = mid
        else:
            # middle element is greater than last means
            # second half of array is decreasing            
            low = mid + 1
    return low

A = [4, 5, 6, 7, 1, 2, 3]
print(by_brute_force(A))
print(by_binary_search(A))