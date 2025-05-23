nums = [5, 9, 1, 2, 3,4, 15, 6, 3]
target = 13
n=len(nums)

'''
def twosum(nums, target):
    res = []
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:      #time-->n*n
                res.append(i)
                res.append(j)
    return res

result = twosum(nums, target)
print(result)
'''

#first ele + second ele=target
#target-first ele=second ele

def twoSum(nums,target,n):
    hashMap={}
    for i in range(0,n):
        remaining=target-nums[i]
        if remaining in hashMap:
            return [hashMap[remaining],i]
        hashMap[nums[i]]=i

res=twoSum(nums,target,n)
print(res)