class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        memo = {}

        def dfs(i,j):
            if i == m:
                return n-j
            if j == n:
                return m-i
            
            if (i,j) in memo:
                return memo.get((i,j))
            
            if word1[i] == word2[j]:
                res = dfs(i+1,j+1)
                memo[(i,j)] = res
                return res
            else:
                # insert char in word1 to match word2
                insert = dfs(i,j+1)
                # delete char in word1 to match word2
                delete = dfs(i+1,j)
                # replace char in word1 to match word2
                replace = dfs(i+1,j+1)

                memo[(i,j)] = 1+min(insert,delete,replace)
                return memo.get((i,j))

        return dfs(0,0)


            