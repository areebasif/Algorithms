def palindrome(s):
    s = s.lower()
    s = ''.join(e for e in s if e.isalpha())
    for i in range(len(s)):
        if s[i]==s[-i-1]:
            return True
    return False

print(palindrome("am!ma"))
