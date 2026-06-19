# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"
        
        queue = deque([root])
        ans_list = []
        while queue:
            cur = queue.popleft()
            
            if cur:
                ans_list.append(str(cur.val))
                queue.append(cur.left)
                queue.append(cur.right)

            else:
                ans_list.append("N")
            
        return ','.join(ans_list)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "" or data == "N":
            return None
        
        data = data.split(",")
        root = TreeNode(val=int(data[0]))
        queue = deque([root])

        i = 1
        while queue and i < len(data):
            cur = queue.popleft()

            if data[i]!= "N":
                cur.left = TreeNode(int(data[i]))
                queue.append(cur.left)
            i += 1

            if i < len(data) and data[i] != "N":
                cur.right = TreeNode(int(data[i]))
                queue.append(cur.right)
            i+=1
        return root



