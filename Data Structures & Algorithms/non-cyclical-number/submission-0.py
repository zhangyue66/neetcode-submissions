class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        
        seen = set()

        def genNumber(n):
            number = str(n)
            ans = 0
            for num in number:
                ans += int(num)**2
            return ans

        while n != 1:
            n = genNumber(n)
            # print(f"num is {num}")
            if n in seen:
                return False
            else:
                seen.add(n)
        return True