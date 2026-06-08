class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        if len(stones) == 1:
            return stones[0]
        stones = [-1*stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = -1*(heapq.heappop(stones))
            second = -1*(heapq.heappop(stones))

            if first > second:
                heapq.heappush(stones, -1*(first - second))

        return -stones[0] if stones else 0
