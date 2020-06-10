def by_linear_search(k):
    n = 1
    while n**2 <= k:
        n += 1
    return n - 1

def by_binary_search(k):
    low = 0
    high = k
    while low <= high:
        mid = (low + high) // 2
        if mid ** 2 > k:
            high = mid - 1
        else:
            low = mid + 1
    return low - 1

print(by_linear_search(12))      
print(by_linear_search(300))
print(by_binary_search(12))
print(by_binary_search(300))