def searchInsert(nums, target):
    intStart=None
    whereItShould=None
    for index, i in enumerate(nums):
        if target<i:
            whereItShould=index
        if i==target:
            intStart=index 
        if intStart is not None:
            return intStart
        elif whereItShould is not None:
            return whereItShould
        else:
            return len(nums)

nums=[1,3,3,4,5,6,8]
target=7
searchInsert(nums,target)