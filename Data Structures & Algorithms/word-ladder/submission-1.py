class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in set(wordList):
            return 0

        queue = deque()
        iteration = 0
        # build the graph with patter:word h*t:[hot,hit]
        graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i]+'*'+word[i+1:]
                graph[pattern].append(word)
        # print(graph)
        visited = set()
        visited.add(beginWord)
        queue.append((beginWord,1))
        while queue:
            cur_word, iteration = queue.popleft()
            # print(cur_word,iteration)
            if cur_word == endWord:
                return iteration
            for i in range(len(cur_word)):
                pattern = cur_word[:i] + '*' + cur_word[i+1:]
                for nei in graph[pattern]:
                    if nei not in visited:
                        queue.append((nei,iteration+1))
                        visited.add(nei)

        return 0
