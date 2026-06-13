# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        if not root:
            return ans
        
        def dfs(node,prev=-float('inf')):
            if not node:
                return

            if node.val >= prev:
                self.ans += 1
                prev = node.val

            dfs(node.left,prev)
            dfs(node.right,prev)

        dfs(root)
        return self.ans