class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # nums = [3,4,5,6,1,2]
        l,r = 0,len(nums)-1

        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                # nums is sorted
                res = min(res,nums[l])
                break

            mid = (l+r) // 2
            res = min(res,nums[mid])
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                # right part is sorted
                r = mid - 1
        
        return res
