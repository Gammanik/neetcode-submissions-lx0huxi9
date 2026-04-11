class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]

        for s in strs:
            if len(s) <= len(pref):
                    pref = pref[:len(s)]

            for i in range(len(s)):
                if i < len(pref) and s[i] != pref[i]:
                    pref = pref[:i]
                    continue


        
        return pref