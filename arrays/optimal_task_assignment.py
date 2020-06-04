def optimal_task_assignment(A):
    A.sort()
    result = []
    for i in range(len(A)//2):
        result.append((A[i], A[~i]))
    return result

print(optimal_task_assignment([6, 3, 2, 7, 5, 5]))
