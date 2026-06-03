# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node, cnt):
            if not node:
                return
            cnt += 1
            left = dfs(node.left, cnt)
            right = dfs(node.right,cnt)

            self.ans = max(self.ans,cnt)

        dfs(root,0)
        return self.ans