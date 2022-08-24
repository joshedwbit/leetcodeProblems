def lengthlong(s):
    array=[]
    while s:
        y=s[0]
        s=s.replace(y,'')
        array.append(y)
    print(array)
    print(len(array))

s='pwwkew'
lengthlong(s)