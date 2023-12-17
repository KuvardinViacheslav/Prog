def binary_search(nums, left, right, value):
    if left <= right:
        mid = (left + right) // 2
        if nums[mid] == value:
            return mid
        elif nums[mid] > value:
            return binary_search(nums, left, mid-1, value)
        else:
            return binary_search(nums, mid + 1, right, value)
    else:
        return -1

nums = [5, 78, 88, 99, 105, 250, 600, 1001]
x = 600
result = binary_search(nums, 0, len(nums)-1, x)
print("Элемент не найден" if result == -1 else f"Элемент расположен в позиции {result}")
