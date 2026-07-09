class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topological sort using dfs
        graph =defaultdict(list)

        for a,b in prerequisites:
            graph[b].append(a)

        visited = set()
        def dfs(course):
            if course in visited:
                return False
            
            visited.add(course)
            for crs in graph[course]:
                if not dfs(crs):
                    return False
            visited.remove(course)
            return True

        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True


