def is_palindrome_permutation(s):
    '''
        for strings of - 
            * even length - all characters should be of even count
            * odd length - all characters should be of even count except one which have odd count
    '''
    s = s.replace(' ', '').lower()
    ht = dict()

    for i in s:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1
    
    odd_count = 0

    for k, v in ht.items():
        if v % 2 != 0 and odd_count == 0:
            odd_count += 1
        elif v % 2 != 0 and odd_count != 0:
            return False
    
    return True


palin_perm = "Tact Coa"
not_palin_perm = "This is not a palindrome permutation"

print(is_palindrome_permutation(palin_perm))
print(is_palindrome_permutation(not_palin_perm))

print(is_palindrome_permutation('ACCCA'))