def spreadsheet_encode_column(s):
    exp = len(s) - 1
    total = 0
    for i in s:
        total += (ord(i) - ord('A') + 1) * (26 ** exp)
        exp -= 1
    return total

print(spreadsheet_encode_column('AA'))
print(spreadsheet_encode_column('ZZ'))
print(spreadsheet_encode_column('ZZXZ'))