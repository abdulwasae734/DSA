class Solution:
    def prefixesDivBy5(self, A):
        result = []
        current = 0


        
        for bit in A:
            current = (current << 1) | bit
            current %= 5
            result.append(current == 0)
    



        return result
