"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        stack = [node]
        clones = {node: Node(val=node.val)}

        while stack:
            cur = stack.pop()
            
            for neighbor in cur.neighbors:
                # 1. If the neighbor hasn't been cloned yet, create it
                if neighbor not in clones:
                    clones[neighbor] = Node(val=neighbor.val)
                    stack.append(neighbor) # Queue it to explore its own neighbors later
                
                # 2. Connect the cloned current node to the cloned neighbor
                clones[cur].neighbors.append(clones[neighbor])
        
        # Directly return the clone of the exact node we started with
        return clones[node]