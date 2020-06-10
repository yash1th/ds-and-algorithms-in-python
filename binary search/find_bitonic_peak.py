def by_linear_search(data):
    for i in range(0, len(data)-1):
        if data[i] > data[i-1] and data[i] > data[i+1]:
            return data[i]
    return None

def by_binary_search(data):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2

        mid_left = data[mid - 1] if mid - 1 > 0 else float("-inf")
        mid_right = data[mid + 1] if mid + 1 < len(data) else float("inf")

        if mid_left < data[mid] < mid_right:
            low = mid + 1
        elif mid_left > data[mid] > mid_right:
            high = mid - 1

        elif data[mid] > mid_left and data[mid] > mid_right:
            return data[mid]

    return None


A1 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
A2 = [1, 6, 5, 4, 3, 2, 1]
A3 = [1, 2, 3, 4, 5]
A4 = [5, 4, 3, 2, 1]

print('---linear approach---')
print(by_linear_search(A1))
print(by_linear_search(A2))
print(by_linear_search(A3))
print(by_linear_search(A4))

print('---binary search approach---')
print(by_binary_search(A1))
print(by_binary_search(A2))
print(by_binary_search(A3))
print(by_binary_search(A4))