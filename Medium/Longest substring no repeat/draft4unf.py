class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
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
        if len(arraylength)!=0:
            return max(arraylength)
        else:
            return len(s)