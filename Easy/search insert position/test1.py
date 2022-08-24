def searchInsert(nums, target):
    intStart=None
    for index, i in enumerate(nums):
        if i==target:
            intStart=index 
            print(intStart) 
            # return index
    if intStart is None:
        for index,j in enumerate(nums):
            if target<j:
                whereItShould=index
                print(whereItShould)
                # return index


nums=[1,3,3,4,5,6,8]
target=7
searchInsert(nums,target)