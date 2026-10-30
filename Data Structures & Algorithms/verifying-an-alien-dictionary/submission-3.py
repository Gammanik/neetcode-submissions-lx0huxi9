class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mp = {}
        valid = [ True ] * len(words)
        
        for i, c in enumerate(order):
            mp[c] = i

        n = max(map(len, words), default=0)
        for i in range(n):            
            for k in range(1, len(words)):
                w = words[k]
                wp = words[k-1]
                if len(wp) <= i:
                    valid[k-1] = False
                    continue

                if not valid[k-1]:
                    continue


                if len(w) <= i:
                    valid[k-1] = False

                    if len(wp) > len(w):
                        print('::')
                        return False
                    else:
                        continue
                


                w_o  = mp[w[i]]
                wp_o = mp[wp[i]]

                if w_o < wp_o:
                    return False
                if w_o > wp_o:
                    valid[k-1] = False
                
        return True