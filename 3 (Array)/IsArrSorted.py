nums=[1,2,3,4,5,6]
n=len(nums)

# for i in range(0,n-1):
#     if nums[i]>nums[i+1]:
#         print("not sorted")
#     print("sorted")


def isSorted(nums):
    for i in range(0,n-1):
        if nums[i]>nums[i+1]:
            return False
        
    return True

print(isSorted(nums))
