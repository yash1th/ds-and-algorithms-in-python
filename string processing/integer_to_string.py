def integer_to_string(num):
    if num == 0:
        return '0'
    elif num < 0:
        neg = True
        num *= -1
    else:
        neg = False
    
    result = []
    
    while num:
        result.append(str(num % 10))
        num //= 10
    if neg:
        result.append('-')
    
    return ''.join(result[::-1])
    

print(integer_to_string(0))
print(integer_to_string(-123))