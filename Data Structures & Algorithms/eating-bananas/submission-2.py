class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math # used for ceiling 2.3 -> 3 in python
        lower = 1
        upper = max(piles)

        while lower <= upper:
            mid = (lower+upper) // 2
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile/mid)

            if total_time <= h:
                upper = mid -1
            else:
                lower = mid + 1

        return lower
