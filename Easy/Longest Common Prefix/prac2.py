def longestCommonPrefix(strs):
    floorLength=200
    array=[]
    for element in strs:
        if element!="":
            for count,element in enumerate(strs):
                if len(element)<floorLength:
                    floorLength=len(element)
    # floorLength returns shortest string given
            for i in range(0,floorLength):
                set=[]
                for j in strs:
                    set.append(j[i])
        # for each word in strs, create an array for the first letter, second letter etc
                for k in set:
                    if k!=set[0]:
                # loop carries on until a letter doesn't match that position in other words
                        print(j[0:i])
                        return j[0:i]
                    else:
                        print(strs)
                        return strs 
        else:
            return strs      



longestCommonPrefix([""])