class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        print('s:', s)

        # if len(s) == 0:
        #     return False

        if not hasattr(self, "removed"):
            self.removed = False

        while i < j:
            if s[i] != s[j] and self.removed:
                return False

            if s[i] != s[j] and not self.removed:
                self.removed = True
                return self.validPalindrome(s[i+1:j+1]) or self.validPalindrome(s[i:j])

            i += 1
            j -= 1


        return True