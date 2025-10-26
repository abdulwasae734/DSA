class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        length1 = len(word1)
        length2 = len(word2)

        small_length = min(length1,length2)
        small_word = min(word1,word2)
        newstr = ''

        for i in range(small_length):
            newstr += word1[i]
            newstr += word2[i]

        newstr += (word1 if length1 >= length2 else word2)[small_length:]

        return newstr

        

        