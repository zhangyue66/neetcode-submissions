class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}

        for i,char in enumerate(s):
            lastIndex[char] = i

        ans = []

        left = right = 0

        for i,c in enumerate(s):
            right = max(right,lastIndex[c])

            if i == right:
                ans.append(right-left+1)
                left = i+1
        return ans



