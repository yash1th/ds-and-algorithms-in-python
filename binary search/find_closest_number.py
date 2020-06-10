def by_linear_search(data, target):
    if len(data) == 0:
        return None
    if len(data) == 1:
        return data[0]
    
    closest_difference = abs(target - data[0])
    closest_number = None
    for i in data[1:]:
        if abs(i - target) < closest_difference:
            closest_difference = abs(i - target)
            closest_number = i
    
    return closest_number

def by_binary_search(data, target):
    if len(data) == 0:
        return None
    if len(data) == 1:
        return data[0]
    
    low = 0
    high = len(data) - 1
    min_diff = float('inf')
    closest_num = None

    while low <= high:
        mid = (low + high) // 2

        if mid + 1 < len(data):
            right_diff = abs(data[mid+1] - target)
        if mid > 0:
            left_diff = abs(data[mid-1] - target) 

        # do right diff and left diff comparison with min diff
        if left_diff < min_diff:
            min_diff = left_diff
            closest_num = data[mid-1]
        if right_diff <  min_diff:
            min_diff = right_diff
            closest_num = data[mid+1]

        if data[mid] < target:
            low = mid + 1
        elif data[mid] > target:
            high = mid - 1
        else:
            return data[mid]
    return closest_num



A1 = [1, 2, 4, 5, 6, 6, 8, 9]
A2 = [2, 5, 6, 7, 8, 8, 9]
print(by_linear_search(A1, 11))
print(by_linear_search(A2, 4))

print(by_binary_search(A1, 11))
print(by_binary_search(A2, 4))