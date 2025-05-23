nums=[-1,-2,-3,-4,-1,-2,-13,-23,-23,-3434,-343]

n=len(nums)
largest=float("-inf")
Slargest=float("-inf")

'''
for i in range(0,n):
    if nums[i]>largest:
        largest=nums[i]
for i in range(0,n):
    if nums[i]>Slargest and nums[i]!=largest:
        Slargest=nums[i]    
print(Slargest)
print(largest)
'''

for i in range(0,n):
    if nums[i]>largest:
        Slargest=largest
        largest=nums[i]
    elif nums[i]>Slargest and nums[i]!=largest:
        Slargest=nums[i]

print(Slargest)
