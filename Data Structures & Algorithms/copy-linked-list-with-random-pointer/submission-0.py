"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ans = temp = Node(x=0)

        cur = head
        visited = {}
        while cur:
            new_node = Node(x=cur.val)
            temp.next = new_node

            visited[cur] = new_node


            cur = cur.next
            temp = temp.next

        second_old = head
        second_new = ans.next

        while second_old:
            if second_old.random:
                second_new.random = visited[second_old.random]
            else:
                second_new.random = None

            second_old = second_old.next
            second_new = second_new.next

        return ans.next



        