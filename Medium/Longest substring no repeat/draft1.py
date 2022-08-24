def lengthlong(s):
    array=[]
    for i in s:
        y=s[0]
        s=s.replace(y,'')
        array.append(y)
    print(array)

s='abcdejj'
lengthlong(s)