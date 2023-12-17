def binary_search(nums, left, right):
    if left <= right:
        mid = (left + right) // 2
        if nums[mid] % 2 == 0 and nums[mid - 1] % 2 != 0:
            return mid
        elif nums[mid] % 2 == 0:
            return binary_search(nums, left, mid - 1)
        else:
            return binary_search(nums, mid + 1, right)
    else:
        return -1


nums = [1, 3, 5, 7, 9, 11, 13, 24, 34, 44, 50, 54, 60, 64, 68, 70, 74]
result = binary_search(nums, 0, len(nums) - 1)
print(result)
