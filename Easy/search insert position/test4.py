class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        intStart=None
        whereItShould=None
        for index, i in enumerate(nums):
            if target<i:
                whereItShould=index
                break
            if i==target:
                intStart=index 
        if intStart is not None:
            return intStart
        elif whereItShould is not None:
            return whereItShould
        else:
            return len(nums)