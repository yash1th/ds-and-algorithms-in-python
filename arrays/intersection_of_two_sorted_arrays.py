def intersection_of_two_sorted_arrays(A, B):
    if not A or not B:
        return False
    
    i = 0
    j = 0
    result = []

    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if A[i] not in result:
                result.append(A[i])
            # or 
            # if i == 0 or A[i] != A[i-1]:
                # result.append(A[i])
            i += 1
            j += 1
            continue
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1

    return result


print(intersection_of_two_sorted_arrays(
    [2, 3, 3, 5, 7, 11],
    [3, 3, 7, 15, 31]
))