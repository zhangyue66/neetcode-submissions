class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ''
        for s in strs:
            n = len(s)
            ans += (str(n) + '#' + s)
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j]) # length of the string
            ans.append(s[j+1:j+1+length])

            i = j + 1 + length
        return ans

