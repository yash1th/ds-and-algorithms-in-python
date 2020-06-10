def linear_search(data, target):
    for i in data:
        if i == target:
            return True
    return False

data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
target = 37
print(linear_search(data, 37))