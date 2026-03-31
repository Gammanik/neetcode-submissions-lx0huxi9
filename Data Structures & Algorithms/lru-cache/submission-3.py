from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.mp = {}    
        self.q = deque()

    def get(self, key: int) -> int:
        v_c = self.mp.get(key)
        print('get', key, v_c, self.mp)
        if not v_c:
            return -1

        self.q.append(key)
        self.mp[key] = (v_c[0], v_c[1] + 1)
        # while len(self.mp) > self.cap:
        #     key_toremove = self.q.popleft()
        #     v_c = self.mp.get(key_toremove)
        #     if v_c[1] > 1:
        #         self.mp[key_toremove] = (v_c[0], v_c[1] - 1)
        #     else:
        #         del self.mp[key_toremove]
        return v_c[0]

    def put(self, key: int, value: int) -> None:
        v_c = self.mp.get(key)
        if not v_c:
            self.mp[key] = (value, 1)
        else:
            self.mp[key] = (value, v_c[1] + 1)
        # print(key, self.q, self.mp)

        self.q.append(key)
        while len(self.mp) > self.cap:
            key_toremove = self.q.popleft()
            v_c = self.mp.get(key_toremove)
            if v_c[1] > 1:
                self.mp[key_toremove] = (v_c[0], v_c[1] - 1)
            else:
                del self.mp[key_toremove]

        print('put', key, self.q, self.mp)