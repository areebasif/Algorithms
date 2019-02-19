def normalize(s):
    s = s.replace(" ","")
    return s.lower()


def is_unique(s):
    ht = {}
    for i in s:
        if i not in ht:
            ht[i] = 1
        else:
            return False
    return True

s1 = "abcDefg"
s1 = " not unique STR"
s1 = normalize(s1)
print(is_unique(s1))