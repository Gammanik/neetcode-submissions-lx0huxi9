from collections import Counter
from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        h = [(-v, k) for k, v in freq.items()]
        heapq.heapify(h)

        time = 0
        q = deque()

        while h or q:
            print(time, h, q)
            time += 1
            if h:
                f, k = heapq.heappop(h)
                if f < -1:
                    q.append((f+1, k, time + n))
            
            if q and q[0][2] == time:
                f, k, new_time = q.popleft()
                time = new_time
                heapq.heappush(h, (f,k))

        return time

        