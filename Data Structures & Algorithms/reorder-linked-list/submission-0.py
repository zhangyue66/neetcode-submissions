# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find mid node
        fast,slow = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse 2nd half of the list
        prev, cur = None, slow
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        # now merge the 2 lists
        first,second = head, prev
        while second.next:
            tmp = first.next
            first.next = second
            first = tmp

            tmp = second.next
            second.next = first
            second = tmp