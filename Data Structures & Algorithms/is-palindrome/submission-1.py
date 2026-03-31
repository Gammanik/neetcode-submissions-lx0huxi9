import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        i, j = 0, len(s)-1

        while j > i:
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1

        return True
        