nums=[1,2,3,7,9,10]
target=9

def twoSumII(nums,target):
    i=0
    j=len(nums)-1
    while(i<j):
        sum=nums[i]+nums[j]
        if sum>target:
            j-=1
        elif sum<target:
            i+=1
        else:
            return [i+1,j+1]
        
print(twoSumII(nums,target))                
