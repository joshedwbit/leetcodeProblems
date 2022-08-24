from calendar import c


def isValid(s):
    cumarray=[]
    for count,element in enumerate(s, start=0):
        cumarray.append(element)
        if count>0:
            if element==")":
                if cumarray[count-1]=="{" or cumarray[count-1]=="[":
                    print('f')
                    return False
            elif element=="}":
                if cumarray[count-1]=="(" or cumarray[count-1]=="[":
                    print('f')
                    return False
            elif element=="]":
                if cumarray[count-1]=="(" or cumarray[count-1]=="{":
                    print('f')
                    return False
    print('t')
    return True


isValid("()[]{}")