nums=[1,1,0,1,0,1,1,1,1,0,1,1,1,1,1,1]

count=0
maxCount=0

for i in range(0,len(nums)):
    if nums[i]==1:
        count+=1
    else:
        maxCount=max(count,maxCount)
        count=0

print(max(maxCount,count))            