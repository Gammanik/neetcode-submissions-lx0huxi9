class MyHashSet:

    def __init__(self):
        self.m = [ [] for i in range(10000)]
        

    def add(self, key: int) -> None:
        if self.contains(key):
            return

        bucket = key % 10000
        self.m[bucket].append(key)

    def remove(self, key: int) -> None:
        bucket = key % 10000

        for i in range(len(self.m[bucket])):
            if self.m[bucket][i] == key:
                del self.m[bucket][i]
                return

    def contains(self, key: int) -> bool:
        bucket = key % 10000

        for i in range(len(self.m[bucket])):
            if self.m[bucket][i] == key:
                return True
        
        return False
        

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)