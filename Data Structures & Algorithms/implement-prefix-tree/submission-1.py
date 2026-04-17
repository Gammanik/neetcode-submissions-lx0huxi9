class PrefixTree:
    def __init__(self):
        self.head = {}

    def insert(self, word: str) -> None:
        curr = self.head
        for c in word:
            if not c in curr:
                curr[c] = {}
            curr = curr[c]

        curr['#'] = '#'
        # print(self.head)

    def search(self, word: str) -> bool:
        curr = self.head
        for ch in word:
            if not ch in curr:
                return False
            curr = curr[ch]
        print(word, curr)
        return not not curr.get('#')


    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for ch in prefix:
            if not ch in curr:
                return False
            curr = curr[ch]
        return True