class PrefixTree:

    def __init__(self):
        self.head = {}
        

    def insert(self, word: str) -> None:
        curr = self.head
        for c in word:
            node = curr.get(c)
            if not node:
                curr[c] = {}

            curr = curr[c]

        curr[' '] = ' '
        # print(curr)

    def search(self, word: str) -> bool:
        curr = self.head
        for c in word:
            if c not in curr:
                return False
            
            curr = curr[c]

        return curr.get(' ') == ' '

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for c in prefix:
            # print(c, curr)
            if c not in curr:
                return False
            
            curr = curr[c]

        return True
        