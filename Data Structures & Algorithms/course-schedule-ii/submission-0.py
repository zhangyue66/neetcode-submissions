class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for course,pre_course in prerequisites:
            graph[pre_course].append(course)
        # print(graph)

        # we need to make sure no cycle in graph
        visited = [0]*numCourses

        self.ans = []

        def dfs(course):
            # dfs to find cycle or no-cycle in graph
            if visited[course] == 1:
                return True
            if visited[course] == 2:
                return False

            visited[course] = 1

            for neighbor in graph[course]:
                if dfs(neighbor):
                    return True

            visited[course] = 2
            self.ans.append(course)
            return False

        for course in range(numCourses):
            if dfs(course):
                return []
        return self.ans[::-1]
