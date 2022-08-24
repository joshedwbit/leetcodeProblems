from calendar import c


def isValid(s):
    cumarray=[]
    cumcount=0
    for count,element in enumerate(s, start=0):
        cumarray.append(element)
        if element=="(":
            cumcount+=1
        elif element=="{":
            cumcount+=2
        elif element=="[":
            cumcount+=3
        elif element==")":
            cumcount-=1
        elif element=="}":
            cumcount-=2
        elif element=="]":
            cumcount-=3
        if count>0:
            if element==")":
                if cumarray[count-1]=="{" or cumarray[count-1]=="[":
                    # print('f')
                    return False
            elif element=="}":
                if cumarray[count-1]=="(" or cumarray[count-1]=="[":
                    # print('f')
                    return False
            elif element=="]":
                if cumarray[count-1]=="(" or cumarray[count-1]=="{":
                    # print('f')
                    return False
    # print('t')
    if cumcount==0:
        return True
    else:
        return False


isValid("()[]{}")