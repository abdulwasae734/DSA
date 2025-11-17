class Solution:
    def maxOperations(self, s: str) -> int:
        ones = 0
        ans = 0
        length = len(s)


        for i, pussy in enumerate(s):
            if pussy == '1': 
                ones += 1
            else:
                if i + 1 == length:
                    ans += ones
                elif s[i+1] == '1':
                    
                    ans += ones
        return ans