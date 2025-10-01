class Solution:
    def singleNumber(self, nums) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]

        
        ans = nums[0]
        for i in range(1,length):
            ans ^= nums[i]
        
        return ans