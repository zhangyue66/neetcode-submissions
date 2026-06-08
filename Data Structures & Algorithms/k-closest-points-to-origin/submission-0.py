class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        heap = [(x**2+y**2,x,y) for x,y in points]
        heapq.heapify(heap)
        
        ans = []
        for i in range(k):
            dist,x,y = heapq.heappop(heap)
            ans.append([x,y])

        return ans
        