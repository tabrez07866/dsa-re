nums=[1,0,3,2,5,7,4]
n=len(nums)
'''
for i in range(0,n+1):
    if i not in nums:       #time compelxity ->n*n
        print(i)
'''

'''
freq={}

for i in range(0,n+1):
    freq[i]=0

for num in nums:               #time complexity -> 3n
    freq[num]=1

for k,v in freq.items():
    if v==0:
        print(k)
'''   

total_sum=(n*(n+1))//2
nums_sum=0
for num in nums:                #time complexity --> n
    nums_sum=nums_sum+num
print(total_sum-nums_sum)    
