class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word = []

        for c in s:
            if c != ' ':
                word.append(c)
            elif word:
                words.append(''.join(word))
                word = []

        if word:
            words.append(''.join(word))

        res_string = ' '.join(words[::-1])
        return res_string