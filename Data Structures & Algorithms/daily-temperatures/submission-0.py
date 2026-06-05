class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force
        res= []
        n = len(temperatures)
        if n == 1:
            return [0]

        for i in range(n-1):
            found = False
            for j in range(i+1,n):
                if temperatures[i] < temperatures[j]:
                    res.append(j-i)
                    found = True
                    break
            if not found:
                res.append(0)
        res.append(0)
        return res