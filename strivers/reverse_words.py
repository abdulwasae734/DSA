class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word = []
        for c in s:
            if c != ' ':
                word.append(c)
            elif word:
                words.append("".join(word))
                word=[]
        
        if word:  
            words.append("".join(word))
        res = []
        for i in range(len(words)-1,-1,-1):
            res.append(words[i])
        return " ".join(res)

