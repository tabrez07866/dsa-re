def bubble_sort(nums):
    n=len(nums)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if(nums[j]>nums[j+1]):
                nums[j],nums[j+1]=nums[j+1],nums[j]


nums=[2,3,54,4,4,64,453,32,2354,565]
bubble_sort(nums)
print(nums)