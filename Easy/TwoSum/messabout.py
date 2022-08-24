
def twoSum(nums, target):
    prevMap = {}
    # element are stored as val:index pairs
    for count, i in enumerate(nums):
        # enumerate returns index and element (similar to for in range) except 2 returns
        z = target-i
        if z in prevMap:
            # print([prevMap[z],count])
            return [prevMap[z],count]
        prevMap[i]=count
        # stores as key value pair

vec = [3,2,4]

twoSum(vec,6)