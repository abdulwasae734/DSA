class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        for i in range(length):
            min = i
            for j in range(i+1,length):
                if (nums[j] < nums[min]):
                    min = j
            nums[i],nums[min] = nums[min],nums[i]