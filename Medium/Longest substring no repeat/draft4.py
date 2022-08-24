def lengthlong(s):
    array=[]
    arraylength=[]
    while s:
        y=s[0]
        if y not in array:
            s=s[1:]
            array.append(y)
        else:
            arraylength.append(len(array))
            array=[]
    print(max(arraylength))

        

s='pwwkew'
lengthlong(s)