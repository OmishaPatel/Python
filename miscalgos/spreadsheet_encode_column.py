def spreedsheet_encode_column(col_str):
    num = 0
    count = len(col_str) -1
    for s in col_str:
        num += 26**count * (ord(s) - ord('A') + 1)
        count -= 1

    return num

print(spreedsheet_encode_column("A"))
print(spreedsheet_encode_column("AA"))
print(spreedsheet_encode_column("ZZ"))