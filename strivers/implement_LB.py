class Solution:
    def findFloor(self, nums, x):
        # code here
        low = 0
        high = len(nums) - 1
        ans = -1
        
        while (low <= high):
            mid = (low + high) // 2

            if x < nums[mid]:
                high = mid - 1
            elif x >= nums[mid]:
                ans = mid
                low = mid + 1
        
        return ans