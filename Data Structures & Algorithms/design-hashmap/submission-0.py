class MyHashMap:

    def __init__(self):
        self.m = [[] for _ in range(10000)]
        
    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1:
            self.remove(key)
        
        bucket = key % 10000
        self.m[bucket].append((key, value))

    def get(self, key: int) -> int:
        bucket = key % 10000
        for el in self.m[bucket]:
            print(el)
            if el[0] == key:
                return el[1]

        return -1

    def remove(self, key: int) -> None:
        bucket = key % 10000
        for el in self.m[bucket]:
            if el[0] == key:
                self.m[bucket].remove(el)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)