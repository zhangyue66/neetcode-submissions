class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course,pre in prerequisites:
            graph[pre].append(course) 

        visited = set()
        path_tracked = set()

        def dfs(course):
            visited.add(course)
            path_tracked.add(course)

            for crse in graph[course]:
                if crse in path_tracked:
                    return True
                if crse not in visited:
                    if dfs(crse):
                        return True

            #remove
            path_tracked.remove(course)
            return False

        for c in range(numCourses):
            if dfs(c):
                return False
        return True