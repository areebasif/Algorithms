def look_and_say_next(s):
    i = 0
    result = []
    while i<len(s):
        count = 1
        while i+1 < len(s) and s[i]==s[i+1]:
            count = count + 1
            i = i+1
        result.append(str(count)+s[i])
        i=i+1
    return ''.join(result)

print(look_and_say_next('1211'))
