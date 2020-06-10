def by_linear_search(data):
    for i, v in enumerate(data):
        if i == v:
            return i
    return None

def by_binary_search(data):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid_index = (low + high) // 2

        if mid_index > data[mid_index]:
            low = mid_index + 1
        elif mid_index < data[mid_index]:
            high = mid_index - 1
        else:
            return mid_index
    return None



# Fixed point is 3:
A1 = [-10, -5, 0, 3, 7]

# Fixed point is 0:
A2 = [0, 2, 5, 8, 17]

# No fixed point. Return "None":
A3 = [-10, -5, 3, 4, 7, 9]


print("Linear Approach")
print(A1)
print(by_linear_search(A1))
print(A2)
print(by_linear_search(A2))
print(A3)
print(by_linear_search(A3))

print("Binary Search Approach")
print(A1)
print(by_binary_search(A1))
print(A2)
print(by_binary_search(A2))
print(A3)
print(by_binary_search(A3))