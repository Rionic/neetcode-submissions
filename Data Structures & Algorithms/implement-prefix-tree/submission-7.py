class PrefixTree:

    def __init__(self):
        self.chars = {}
        self.isEnd = False

    def insert(self, word: str) -> None:
        cur = self
        for c in word:
            if c not in cur.chars:
                cur.chars[c] = PrefixTree()
            cur = cur.chars[c]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self
        for c in word:
            if c not in cur.chars:
                return False
            cur = cur.chars[c]
        return cur.isEnd == True

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for c in prefix:
            if c not in cur.chars:
                return False
            cur = cur.chars[c]
        return True


        