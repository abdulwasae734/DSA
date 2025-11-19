class Solution:
    def findFinalValue(self, nums, original: int) -> int:
        while True:
            if original in nums:
                original = 2 * original
            else:
                break
        return original