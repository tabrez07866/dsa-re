nums = [3,2,3,4,34,34,32,12,45,56]

def merge_array(left,right):
    res=[]
    i,j=0,0
    n,m=len(left),len(right)
    while i<n and j<m:
        if left[i]<=right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    if i<n:
        while i<n:
            res.append(left[i])
            i+=1
    if j<m:
        while(j<m):
            res.append(right[j])
            j+=1
    return res

def mergeSort(nums):
    if len(nums)<=1:
        return nums
    mid=len(nums)//2
    left_arr=nums[:mid]
    right_arr=nums[mid:]
    left=mergeSort(left_arr)
    right=mergeSort(right_arr)
    return merge_array(left,right)

nums=mergeSort(nums)
print(nums)