class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
                
        ans = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(index,cur):
            if len(cur) == len(digits):
                ans.append(cur)
                return
            
            chars = digitToChar[digits[index]]
            for char in chars:
                dfs(index+1,cur+char)

        dfs(0,"")
        return ans