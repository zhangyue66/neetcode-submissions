# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = k
        res = root.val

        def dfs(root):
            nonlocal counter,res
            if not root:
                return

            dfs(root.left)
            if counter == 0:
                return


            res = root.val
            counter -= 1
            if counter == 0:
                return 

            dfs(root.right)

        dfs(root)
        return res
