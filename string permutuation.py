def perm (s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if len(s1) != len(s2):
        return false

    ht = {}
    for i in s1:
        if i not in ht:
            ht[i] = 1
        else:
            ht[i] = ht[i] + 1

    for i in s2:
        if i not in ht:
            ht[i] = 1
        else:
            ht[i] = ht[i] - 1

    return all(value ==0 for value in ht.values())

print(perm('tom','mom'))
