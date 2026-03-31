from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand = sorted(hand)
        freq = Counter(hand)

        # for k, v in freq.items():
        #     if v > groupSize:
        #         return False

        if (len(hand) // groupSize) * groupSize != len(hand):
            return False

        mp = { i: [] for i in range(len(hand) // groupSize) }


        for i in range(len(hand) // groupSize):
            # print(hand, mp)
            # # print(mp)


            first = min(k for k, v in freq.items() if v != 0) #hand.pop(0)
            print(first)
            for c in range(first, first + groupSize):
                if not freq.get(c) or freq.get(c) == 0:
                    print(c)
                    return False

                # if c == hand[0]:
                #     print('~', c)
                #     hand.pop(0)

                mp[i].append(c)
                freq[c] = freq[c] - 1


        return True

        