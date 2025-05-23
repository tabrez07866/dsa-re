nums = [1, 2, 3, 4, 4, 4, 5, 6, 7, 7, 11]
target = 11
left = 0
right = len(nums) - 1

def binary(nums, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # not found

index = binary(nums, target, left, right)
print("Target found at index:", index)
