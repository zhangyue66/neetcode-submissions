# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        levels = []

        from collections import deque

        queue = deque([(1,root)])
        while queue:
            level,cur = queue.popleft()
            if len(levels) < level:
                levels.append([cur.val])
            else:
                levels[level-1].append(cur.val)
            if cur.left:
                queue.append((level+1,cur.left))
            if cur.right:
                queue.append((level+1,cur.right))

        return [ level[-1] for level in levels]