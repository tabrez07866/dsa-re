'''
k=7
nums=[3,9,5,6,7,2]
n=len(nums)
k=k%n
while(k>0):
    nums[:] =[nums[n-1]]+nums[0:n-1]
    k-=1

print(nums)
'''

nums=[3,9,5,6,7,2]
n=len(nums)
k=7
k=k%n

def reverse(nums,left,right):
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1

reverse(nums,0,n-k-1)
reverse(nums,n-k,n-1)
reverse(nums,0,n-1)

print(nums)
