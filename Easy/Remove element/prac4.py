def removeElement(nums,val):
    for i in nums:
        print(i)
        if i==val:
            nums.remove(i)
    print(nums)

nums=[0,1,2,2,3,0,4,2]
val=2
removeElement(nums,val)
