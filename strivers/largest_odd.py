class Solution:
    def largestOddNumber(self, num: str) -> str:
        numm = list(num)
        for i in range(len(numm)-1, -1, -1):
            if int(numm[i])%2 != 0:
                return num[:i+1]
        else:
            return ""