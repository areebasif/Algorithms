def palin_perm(s):
    count = {}
    odd_count = 0
    s = s.replace(" ","").lower()
    for i in s:
        if i in count:
            count[i] = count[i] + 1
        else:
            count[i] = 1

    for i in count:
        if count[i] % 2 != 0 and odd_count == 0:
            odd_count = odd_count + 1
        elif count[i] %2 != 0 and odd_count != 0:
            return False
    return True

print(palin_perm("Taxt Coa"))