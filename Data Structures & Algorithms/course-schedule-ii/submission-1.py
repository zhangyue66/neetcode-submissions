class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        indegrees = [0]*numCourses

        for a,b in prerequisites:
            graph[b].append(a)
            indegrees[a] += 1

        queue = deque()
        for course in range(numCourses):
            if indegrees[course] == 0:
                queue.append(course)

        topo = []
        while queue:
            cur = queue.popleft()
            topo.append(cur)

            for crs in graph[cur]:
                indegrees[crs] -= 1
                if indegrees[crs] == 0:
                    queue.append(crs)
        
        if len(topo) == numCourses:
            return topo
        return []

        
            