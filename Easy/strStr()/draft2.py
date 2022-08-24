
def strStr(haystack, needle):
    if len(haystack)==0:
        return 0
    intStart=haystack.find(needle)
    if intStart is None:
        return -1
    else:
        return intStart



haystack="hello"
needle="ll"
strStr(haystack,needle)
    
