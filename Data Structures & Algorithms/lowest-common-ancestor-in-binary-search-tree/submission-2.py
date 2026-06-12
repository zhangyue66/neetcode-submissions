# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # use BFS
        from collections import deque
        if not root:
            return
        queue =deque([root])
        while queue:
            cur = queue.popleft()
            if p.val < cur.val and q.val <cur.val:
                queue.append(cur.left)
            elif p.val > cur.val and q.val > cur.val:
                queue.append(cur.right)
            else:
                return cur