class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        counter = Counter(nums)
        heap = []
        for key,v in counter.items():
            heapq.heappush(heap,(-v,key))
        ans = []
        while k > 0:
            _,key = heapq.heappop(heap)
            ans.append(key)
            k -= 1
        return ans