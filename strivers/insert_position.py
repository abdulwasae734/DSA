class Solution:
    def searchInsert(self, nums, target: int) -> int:
        length = len(nums)
        low = 0
        high = length - 1

        while (low <= high):
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
            
        return low