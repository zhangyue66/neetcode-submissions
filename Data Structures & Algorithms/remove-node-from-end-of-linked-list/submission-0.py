# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast,slow = head, head
        for i in range(n):
            fast = fast.next # fast is the node we want to remove

        
        if not fast:
            return slow.next
            
        prev= None
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next

        tmp = slow.next
        prev.next = tmp

        

        return head

        
        