class WordDictionary:

    def __init__(self):
        self.word_list = []
        self.word_set = set()

    def addWord(self, word: str) -> None:
        self.word_list.append(word)
        self.word_set.add(word)

    def search(self, word: str) -> bool:
        if not self.word_list:
            return False
        if word in self.word_set:
            return True
        
        # print(f'keep searching {word}')
        for wd in self.word_set:
            if len(word) == len(wd):
                match = True
                for i in range(len(word)):
                    if word[i] != wd[i] and word[i] !='.':
                        match = False
                        break
                if match is True:
                    return True
        return False
        
