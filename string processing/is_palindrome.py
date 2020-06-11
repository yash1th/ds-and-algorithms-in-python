def basic_palindrome(s):
    """
        Basic palindrome implementation
    """
    low = 0
    high = len(s) - 1
    while low <= high:
        if s[low] != s[high]:
            return False
        low += 1
        high -= 1
    return True

def is_palindrome(s):
    low = 0
    high = len(s) - 1
    while low < high:
        while not s[low].isalnum() and low < high:
            low += 1
        while not s[high].isalnum() and low < high:
            high -= 1
        
        if s[low].lower() != s[high].lower():
            return False
        
        low += 1
        high -= 1

    return True


print(basic_palindrome('A'))
print(basic_palindrome('ABA'))
print(basic_palindrome(''))

print(is_palindrome('Was it a cat I saw?'))