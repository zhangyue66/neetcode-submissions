class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        l, r = 0, n-1

        while l < r:
            mid = (l + r) // 2
            if nums[l] > nums[r]:
                if nums[mid] > nums[r]:
                    l = mid + 1
                else:
                    r = mid
            else:
                return nums[l]
        return nums[l]
