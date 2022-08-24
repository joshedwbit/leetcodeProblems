def isValid(s):
    cumcount=0
    tick1=0
    tick2=0
    tick3=0
    for i in s:
        if i=="(":
            tick1=1
            cumcount+=1
        elif i=="{":
            tick2=1
            cumcount+=2
        elif i=="[":
            tick3=1
            cumcount+=3
        elif i==")":
            if tick1==1:
                cumcount-=1
        elif i=="}":
            if tick2==1:
                cumcount-=2
        elif i=="]":
            if tick3==1:
                cumcount-=3
    if cumcount==0:
        print('true')
        return True
    else:
        print('false')
        return False


isValid("([)]")