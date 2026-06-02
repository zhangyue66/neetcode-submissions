class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans = 1
        nums_set = set(nums)


        for num in nums:
            # check if num is the start of the sequence
            if num-1 not in nums_set:
                # this could be start of the longest sequence
                length = 1
                for i in range(1,len(nums)):
                    if num + i in nums_set:
                        length += 1
                        ans = max(ans,length)
                    else:
                        ans = max(ans,length)
                        break
        return ans


