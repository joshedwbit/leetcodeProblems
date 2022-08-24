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
                number=0
                for k in set:
                    if k==set[0]:
                # loop carries on until a letter doesn't match that position in other words
                        # print(j[0:i])
                        number=j[0:i-1]
                        print(number)
                    # return number
        else:
            # print("hello")
            return ""      



longestCommonPrefix(["flower","flow","flight"])