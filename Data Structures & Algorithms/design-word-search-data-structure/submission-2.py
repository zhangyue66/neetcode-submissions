class WordDictionary:

    def __init__(self):
        self.cache = set()
        

    def addWord(self, word: str) -> None:
        self.cache.add(word)
        

    def search(self, word: str) -> bool:
        if word in self.cache:
            return True

        
        for existWord in self.cache:
            if len(existWord) == len(word):
                isFound = True
                for i in range(len(word)):
                    if existWord[i] != word[i] and word[i] != '.':
                        isFound = False
                        break
                if isFound:
                    return True
            
        
        return False

            
        
