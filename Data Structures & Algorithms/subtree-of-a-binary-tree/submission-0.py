# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        def dfs(root1,root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False

            if root1.val == root2.val:
                left = dfs(root1.left,root2.left)
                right = dfs(root1.right, root2.right)
                return left and right
            return False

        return dfs(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)