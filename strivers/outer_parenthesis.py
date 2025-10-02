class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        oc = 0

        for c in s:
            if c == '(':
                if oc > 0:
                    result.append(c)
                oc += 1
            else:  
                oc -= 1
                if oc > 0:
                    result.append(c)

        return "".join(result)
