class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counted = set()
        for num in nums:
            if num not in counted:
                counted.add(num)
            else:
                return True
        return False

        