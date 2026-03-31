
# 4|4|3|# ['neet'] 4
# 4|3|# ['neet', 'code'] 4
# 3|# ['neet', 'code', 'love'] 4

class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''

        res = str(len(strs)) + '|'
        for s in strs:
            res += str(len(s)) + '|'

        res += '#'
        res += ''.join(strs)
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        res = []
        splitIdxAmount = self.nxt(s, 0)
        strStart = self.strStartIdx(s)
        s2 = s[strStart:]
        s = s[len(str(splitIdxAmount))+1:strStart]

        for i in range(splitIdxAmount):
            split = self.nxt(s, 0)
            s = s[len(str(split))+1:]

            res.append(s2[:split])
            s2 = s2[split:]
            print(s, res, split)


        # res.append(s)
        return res

    def nxt(self, s: str, i: int) -> int:
        res = []
        j = i
        while s[j] != '|':
            res.append(s[j])
            j += 1
        
        return int(''.join(res))

    def strStartIdx(self, s: str) -> int:
        j = 0
        while s[j] != '#':
            j += 1
        
        return j + 1
