import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = re.sub(r'[^a-zA-Z0-9]', '', s)

        i = 0
        j = len(ss) - 1

        while i < j:
            print(ss[i], ss[j])
            if ss[i].lower() != ss[j].lower():
                return False
            i += 1
            j -= 1

        return True
        