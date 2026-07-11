class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # dfs with hashmap

        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)

        ans = 0

        for node in range(n):
            if node not in visited:
                ans += 1
                dfs(node)
        return ans 