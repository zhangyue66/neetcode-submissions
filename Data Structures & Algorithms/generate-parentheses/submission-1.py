class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        import copy
        self.ans = []

        def dfs(cur=[],open=0,close=0):
            if open == close ==n:
                self.ans.append("".join(cur))
                return

            if open < n:
                cur.append('(')
                dfs(cur[:],open+1,close)
                cur.pop()


            if close < open:
                # two choices - add open or close
                cur.append(')')
                dfs(cur[:],open,close+1)

                cur.pop()




        dfs([],0,0)
        # print(self.ans)
        return self.ans 