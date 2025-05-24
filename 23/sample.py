

def twoSum(nums,target):
    past_freq={}
    result=[]
    for i in range(len(nums)):
        sec_num=target-nums[i]
        if sec_num not in past_freq:
            past_freq[nums[i]]=sec_num
        else:
            result.append(nums.index(sec_num))
            result.append(i)
    return result        

nums=[1,2,3,4,5,6,7,8,9,100]
target=109

print(twoSum(nums,target))