vowels = 'aieou'

#by recursion

def consonants_by_recursion(str):
    if str =='':
        return 0
    if str[0].lower() not in vowels and str[0].isalpha():
         return 1 + consonants_by_recursion(str[1:])
    else:
        return consonants_by_recursion(str[1:])

print(consonants_by_recursion('areeb asif'))

#by iteration

def consonants_by_iteration(str):
    count = 0
    for i in range(len(str)):
        if str[i].lower() not in vowels and str[i].isalpha():
            count = count+1
    return count

print(consonants_by_iteration('areeb asif'))