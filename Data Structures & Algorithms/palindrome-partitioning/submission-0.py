class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(s):
            for i in range(len(s) // 2):
                if s[i] != s[len(s)-1 - i]:
                    return False

            return True

        def dfs(j: int, i: int, curr: List[str]):
            if i == len(s):
                if curr and j == len(s): 
                    # print(curr, j, i)
                    res.append(curr[:])
                return

            if not isPalindrome(s[j:i+1]):
                dfs(j, i+1, curr[:])
            else:
                dfs(j, i+1, curr[:])
                curr.append(s[j:i+1])
                dfs(i+1, i+1, curr[:])
                curr.pop()

        dfs(0,0, [])
        return res
        