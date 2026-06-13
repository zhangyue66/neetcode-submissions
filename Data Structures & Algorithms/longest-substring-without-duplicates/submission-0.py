class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        n = len(s)
        visited = set()
        ans = 0

        for right in range(n):
            if s[right] not in visited:
                visited.add(s[right])
            else:
                while s[left] != s[right]:
                    visited.remove(s[left])
                    left += 1
                left += 1
                
            ans = max((right-left+1),ans)

        return ans
