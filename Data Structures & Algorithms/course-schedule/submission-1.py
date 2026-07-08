class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # using topological sort (indegree) kahn's algo

        graph = defaultdict(list)
        indegrees=[0]*numCourses

        for a,b in prerequisites:
            graph[b].append(a)
            indegrees[a] += 1

        topo = []
        queue = deque()
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                queue.append(i)

        while queue:
            cur = queue.popleft()
            topo.append(cur)
            for course in graph[cur]:
                indegrees[course] -= 1
                if indegrees[course] == 0:
                    queue.append(course)
        return len(topo) == numCourses
