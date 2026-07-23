class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]

        def find(a):
            if parent[a] != a:
                return find(parent[a])
            return a

        def union(a,b):
            pa,pb = find(a),find(b)
            parent[pa] = pb

        for a,b in edges:
            union(a,b)

        ans = set()
        for i in range(n):
            ans.add(find(i))

        return len(ans)