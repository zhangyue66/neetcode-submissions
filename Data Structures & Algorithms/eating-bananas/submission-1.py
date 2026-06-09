class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search
        upper = max(piles)
        lower = 1
        res = upper
        import math

        while lower <= upper:
            mid = (lower+upper)//2

            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile/mid)
            
            if total_time <= h:
                # eat too fast. upper can shrink. we still look for possible smaller one.
                upper = mid - 1
                res = min(res,mid)
            elif total_time > h:
                lower = mid + 1

        return lower

        