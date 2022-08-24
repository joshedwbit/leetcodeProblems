from calendar import c


def isValid(s):
    cumarray=[]
    cumcount=0
    tick1=0
    tick2=0
    tick3=0
    for count,element in enumerate(s, start=0):
        cumarray.append(element)
        if element=="(":
            tick1+=1
            cumcount+=1
        elif element=="{":
            tick2+=1
            cumcount+=2
        elif element=="[":
            tick3+=1
            cumcount+=3
        elif element==")":
            if tick1>=1:
                cumcount-=1
                tick1-=1
            else:
                # print('ex1', count)
                return False
        elif element=="}":
            if tick2>=1:
                cumcount-=2
                tick2-=1
            else:
                # print('ex2')
                return False
        elif element=="]":
            if tick3>=1:
                cumcount-=3
                tick3-=1
            else:
                # print('ex3')
                return False
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
    if cumcount==0:
        # print('t')
        return True
    else:
        return False


isValid("[([]])")