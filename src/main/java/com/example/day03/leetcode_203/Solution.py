from typing import Optional


class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self,head: Optional[ListNode],val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        if not head:
            return head
        cur = head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head