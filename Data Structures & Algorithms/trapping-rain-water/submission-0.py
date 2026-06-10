class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1:
            return 0
        # use brute force
        ans = 0
        n = len(height)

        for i in range(1,n-1):
            left = 0
            for j in range(i,-1,-1):
                left = max(height[j],left)
            right = 0
            for j in range(i,n):
                right = max(height[j],right)
            
            cur_trap_water = min(left,right) - height[i]
            # print(f"current trapped water is {cur_trap_water}. left is {left}. right is {right}. index is {i}")
            ans += cur_trap_water


        return ans