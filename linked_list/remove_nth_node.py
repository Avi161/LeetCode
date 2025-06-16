# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        cur, count = head, 0

        while cur:
            cur = cur.next
            count += 1
        
        cur1 = dummy
        for _ in range(count-n):
            cur1 = cur1.next
        
        cur1.next = cur1.next.next

        return dummy.next
    