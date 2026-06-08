# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        # pop each level at once and use bfs
        from collections import deque
        queue = deque()
        queue.append(root)
        ans = []

        while queue:
            temp = []
            level = []
            while len(queue) > 0:
                cur = queue.popleft()
                level.append(cur.val)
                if cur.left:
                    temp.append(cur.left)
                if cur.right:
                    temp.append(cur.right)
            ans.append(level)
            queue.extend(temp)
        return ans
            
