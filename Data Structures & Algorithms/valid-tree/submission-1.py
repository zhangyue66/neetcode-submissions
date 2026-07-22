class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # first detect if graph has cycle
        visited = [0]*n
        def dfs(node, parent):
            visited[node] = 1
            for nei in graph[node]:
                if nei == parent:
                    continue
                if visited[nei] == 1:
                    return True # has cycle
                if visited[nei] == 0:
                    if dfs(nei, node):
                        return True
            visited[node] = 2
            return False
        
        if dfs(0,-1): # has cycle
            return False

        print(visited)
        for state in visited:
            if state == 0:
                return False
        return True
            
