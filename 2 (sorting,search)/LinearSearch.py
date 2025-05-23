nums=[1,2,3,4,5,6,7,4,4,2,7,11]
target=11

def search(nums,target):
    for i in range(0,len(nums)):
        if nums[i]==target:
            return i
            break
    return -1

print(search(nums,target))    