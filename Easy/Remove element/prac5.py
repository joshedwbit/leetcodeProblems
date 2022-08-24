def removeElement(nums,val):
    for index, i in  enumerate(nums):
        print(index,i)
        # if i==val:
        #     nums.pop(index)
    print(nums)

nums=[0,1,2,2,3,0,4,2]
val=2
removeElement(nums,val)
