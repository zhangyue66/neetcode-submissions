class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            remain = 0 - nums[i]
            # looking for two j,k in nums[i+1:n] so they add up and equal to remain
            j,k = i+1, n-1
            while j < k:
                if nums[j] + nums[k] == remain:
                    ans.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j<k and nums[j] == nums[j-1]:
                        j += 1
                    while j<k and nums[k] == nums[k+1]:
                        k -= 1

                elif nums[j] + nums[k] > remain:
                    k -= 1
                else:
                    j += 1
        return ans


