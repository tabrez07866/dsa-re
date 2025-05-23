nums=[5,10,-3,-1,-10,6]
pos=[]
neg=[]
for i in range(0,len(nums)):
    if nums[i]>0:
        pos.append(nums[i])
    else:
        neg.append(nums[i])

print(pos,neg)    
for i in range(0,len(pos)):
    nums[2*i]=pos[i]
    nums[2*i+1]=neg[i]
print(nums)    
    