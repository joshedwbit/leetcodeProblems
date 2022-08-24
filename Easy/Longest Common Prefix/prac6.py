def longestCommonPrefix(strs):
    floorLength=200
    array=[]
    for count,element in enumerate(strs):
        if len(element)<floorLength:
            floorLength=len(element)
        for i in range(0,floorLength):
            set=[]
            for j in strs:
                set.append(j[i])
            for k in set:
                if k!=set[0]:
                    # print(j[0:i])
                    return j[0:i]
                if i==floorLength-1:
                    if len(j)==1:
                        # print(strs[0])
                        return strs[0]
                    else:
                        # print(j[0:floorLength])
                        return j[0:floorLength]
    return ""



# longestCommonPrefix(["flower","flow","flight"])
# longestCommonPrefix([""])
# longestCommonPrefix(["a"])
# longestCommonPrefix(["a","ab"])
longestCommonPrefix(["ab","a"])
# longestCommonPrefix(["flower","flower","flower"])