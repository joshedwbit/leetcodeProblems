def isValid(s):
    cumcount=0
    cumarray=[0]
    for i in s:
        if i=="(":
            cumcount+=1
        elif i=="{":
            cumcount+=2
        elif i=="[":
            cumcount+=3
        elif i==")":
                cumcount-=1
        elif i=="}":
                cumcount-=2
        elif i=="]":
                cumcount-=3
    if cumcount==0:
        print('true')
        return True
    else:
        print('false')
        return False


isValid("([)]")