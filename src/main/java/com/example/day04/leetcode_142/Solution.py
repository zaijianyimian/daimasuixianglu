from typing import Optional


class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution:
    def detectCycle(self,head : Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        cur = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cur = slow
                break
        if not cur:
            return None
        slow = head
        while slow != cur:
            slow = slow.next
            cur = cur.next
        return slow