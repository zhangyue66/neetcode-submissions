class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEndofWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if cur.children[ord(char)-ord('a')] is None:
                cur.children[ord(char)-ord('a')] = TrieNode()
            cur = cur.children[ord(char)-ord('a')]
        cur.isEndofWord = True


    def search(self, word: str) -> bool:
        cur = self.root

        for char in word:
            if cur.children[ord(char)-ord('a')] == None:
                return False
            cur = cur.children[ord(char)-ord('a')]
        return cur.isEndofWord is True
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for char in prefix:
            if cur.children[ord(char)-ord('a')] == None:
                return False
            cur = cur.children[ord(char)-ord('a')]
            
        return True
        