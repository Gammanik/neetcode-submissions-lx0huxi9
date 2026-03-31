class WordDictionary:

    def __init__(self):
        self.head = {}
        

    def addWord(self, word: str) -> None:
        curr = self.head

        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        
        curr[' '] = ' '

    def search(self, word: str) -> bool:
        return self.h(word, self.head)

    def h(self, word: str, curr: dict):
        if not curr:
            return False

        for i, c in enumerate(word):
            print(i, word, c, curr.get(c))
            if c == '.':
                existent = curr.keys()
                for c_ in existent:
                    if c_ != ' ' and self.h(word[i+1:], curr.get(c_)):
                        return True
                return False
            else:
                if c not in curr:
                    return False

                curr = curr[c]

        print('??', curr)
        return curr != ' ' and curr.get(' ') == ' '
