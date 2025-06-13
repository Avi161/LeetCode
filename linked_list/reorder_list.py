# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        cur = head
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next



        rev = self.reverseList(slow.next)
        slow.next = None

        while rev:
            c_nxt, r_nxt = cur.next, rev.next
            cur.next= rev
            rev.next = c_nxt
            cur, rev = c_nxt, r_nxt


    def reverseList(self, head):
        prev, cur = None, head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev, cur = cur, nxt

        return prev
        