def array_advance(A):
    i = 0
    furthest_reached = 0
    last_index = len(A) - 1
    while i <= furthest_reached and furthest_reached < last_index:
        furthest_reached = max(furthest_reached, A[i] + i)
        i += 1
    return furthest_reached >= last_index

print(array_advance([3, 3, 1, 0, 2, 0, 1]))