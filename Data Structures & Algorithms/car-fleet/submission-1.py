class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        s = []
        for car in pair:
            nxt_time = s[-1] if len(s) > 0 else (target - car[0]) / car[1]

            time = (target - car[0]) / car[1]
            print(time)
            if time <= nxt_time:
                if len(s) > 0:
                    s.pop()
                s.append(nxt_time)
            else:
                s.append(time)

        print(s)
        return len(s)


        
        