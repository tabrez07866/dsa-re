#find unique element in the nums array

'''
nums=[1,1,2,2,3,3,3,4,4,4,5,6,6,7,7]
n=len(nums)
freq_map={}
for i in range(0,n):
    freq_map[nums[i]]=0

j=0
for k in freq_map:
    nums[j]=k
    j+=1

print(j)
'''

#using two pointer
nums=[1,1,2,2,3,3,3,4,4,4,5,6,6,7,7,8,8,8,9,9,0,0,0,12,112131,1212,12131]
n=len(nums)
if n==1:
    print(1)
i=0
j=1
while(j<n):
    if nums[j]!=nums[i]:
        i+=1
        nums[i],nums[j]=nums[j],nums[i]
    j+=1
print(i+1)    

# n = len(nums)
# if n == 0:
#     print(0)
#     exit()

# i = 0
# for j in range(1, n):
#     if nums[j] != nums[i]:
#         i += 1
#         nums[i] = nums[j]

# print(i + 1)
