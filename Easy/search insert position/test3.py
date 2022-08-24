def searchInsert(nums, target):
    intStart=None
    whereItShould=None
    for index, i in enumerate(nums):
        if target<i:
            whereItShould=index
            break
        if i==target:
            intStart=index 
    if intStart is not None:
        print(intStart)
    elif whereItShould is not None:
        print(whereItShould)
    else:
        print(len(nums))

nums=[1,3,5,6]
target=7
searchInsert(nums,target)