def constainduplicate(nums,k):
    seen=set()
    for i,num in enumerate(nums):
        if num in seen:
            return True
        seen.add(num)
        if len(seen)>k:
            seen.remove(nums[i-k])
    return False 

nums=[1,2,3,4,1]
print(constainduplicate(nums,4))       