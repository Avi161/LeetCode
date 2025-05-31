# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = list1, list2
        dummy = ListNode(0)
        tail = dummy

        while cur1 and cur2:
            if cur1.val < cur2.val:
                tail.next = ListNode(cur1.val)
                tail, cur1 = tail.next, cur1.next
            else:
                tail.next = ListNode(cur2.val)
                tail, cur2 = tail.next, cur2.next
        if cur1:
            tail.next = cur1
            tail = tail.next
        if cur2:
            tail.next = cur2
            tail = tail.next    
        return dummy.next   

