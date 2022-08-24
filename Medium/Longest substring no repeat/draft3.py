def lengthlong(s):
    n=0
    while s:
        y=s[0]
        s=s.replace(y,'')
        n+=1
    return n

s='pwwkew'
lengthlong(s)