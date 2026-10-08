class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j, res = 0, 0, ""
        while i < len(word1) and j < len(word2):
            res += (word1[i] + word2[j])
            i += 1
            j += 1

        if i-1 != len(word1):
            res += word1[i:]

        if j-1 != len(word2):
            res += word2[i:]
        
        return res