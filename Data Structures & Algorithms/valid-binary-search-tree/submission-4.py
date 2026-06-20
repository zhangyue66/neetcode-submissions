# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        lst = []
        
        def inorder_dfs(root):
            if not root:
                return
            inorder_dfs(root.left)
            lst.append(root)
            inorder_dfs(root.right)

        inorder_dfs(root)


        return all(lst[i].val < lst[i + 1].val for i in range(len(lst) - 1)) if len(lst) >= 2 else True