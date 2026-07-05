class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        def has_path_bfs(source: int, target: int) -> bool:
            """Standard BFS to check if source can reach target."""
            if source not in graph or target not in graph:
                return False
                
            queue = deque([source])
            visited = {source}
            
            while queue:
                curr = queue.popleft()
                if curr == target:
                    return True
                    
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            return False

        # Process edges chronologically
        for u, v in edges:
            # If u can already reach v, adding this edge creates the redundant cycle
            if has_path_bfs(u, v):
                return [u, v]
            
            # Otherwise, it's a safe edge. Add it to our graph.
            graph[u].append(v)
            graph[v].append(u)
            
        return []

            