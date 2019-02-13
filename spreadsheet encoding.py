def spreadsheat_encoder(s):
    num = 0
    count =  len(s) - 1
    for item in s:
        num = num + 26**count * (ord(item)-64)
        count = count - 1
    return num


print(spreadsheat_encoder('AB'))
