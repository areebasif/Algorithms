def is_anagram(s1,s2):
    count = {}

    if len(s1) != len(s2):
        return False

    for i in s1:
        if i in count:
            count[i] = count[i]+1
        else:
            count[i] = 1


    for i in s2:
        if i in count:
            count[i] = count[i]-1
        else:
            return False

    for i in count:
        if count[i] != 0:
            return False

    return True


print(is_anagram("fairy tales", "rail safety"))