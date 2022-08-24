class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        origArrayLength=len(nums)
        for i in nums:
            if i==val:
                nums.remove(i)
        modifiedArrayLength=len(nums)
        leftover=origArrayLength-modifiedArrayLength
        for i in range(leftover):
            nums.append(0)


int=[0,1,2,2,3,0,4,2]
val=2