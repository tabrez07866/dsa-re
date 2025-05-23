
'''
nums=[1,0,2,4,3,0,0,3,5,0,0,1]
n=len(nums)
temp=[]
j=0
for i in range(0,n):
    if nums[i]!=0:
        temp.append(nums[i])
        j+=1
for i in range(j,n):
    temp.append(0)

nums=temp
print(nums)
'''

nums=[1,3,0,2,4,3,0,0,3,5,0,0,1]
n=len(nums)
i=0
while i<n:
    if nums[i]==0:
        break
    i+=1
j=i+1
while j<n:
    if nums[j]!=0:
        nums[i],nums[j]=nums[j],nums[i]
        i+=1
    j+=1
print(nums)