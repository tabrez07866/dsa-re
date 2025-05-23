nums=[55,32,-97,12,122,232,12132,2423232]
# nums.sort()
# n=len(nums)
# print(nums[n-1])

largest=float("-inf")
n=len(nums)

for i in range(0,n):
    if(nums[i]>largest):
        largest=nums[i]
print(largest)