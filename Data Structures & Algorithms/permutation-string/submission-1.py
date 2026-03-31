from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        c1 = Counter(s1)
        c2 = Counter(s2[:len(s1)])
        print(c1, c2, len(s1))

        for j in range(len(s1), len(s2)):
            if c1 == c2:
                return True
            
            remove_idx = j - len(s1)
            print('1:', j, c2, s2[remove_idx])

            # print(c2[s2[remove_idx]], 1, c2[s2[remove_idx]] == 1)
            if c2[s2[remove_idx]] == 1:
                del c2[s2[remove_idx]]
            else:
                c2[s2[remove_idx]] -= 1

            print('2:', j, c2, s2[remove_idx])

            insert_idx = j
            # print('2:', j, c2, s2[insert_idx])
            if c2[s2[insert_idx]] >= 1:
                c2[s2[insert_idx]] += 1
            else:
                c2[s2[insert_idx]] = 1
            print('3:', j, c2, s2[insert_idx])

        print(c2)
        return c1 == c2

            




        # while j < len(s1):
        #     if c1 == c2:
        #         return True
            
        #     c2[c] = 

        #     i += 1; j += 1