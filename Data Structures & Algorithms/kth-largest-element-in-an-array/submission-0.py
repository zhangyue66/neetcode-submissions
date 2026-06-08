class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # use sorting
        nums.sort(reverse=True)
        print(nums)

        return nums[k-1]
        