from typing import Optional


class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution:
    def getIntersectionNode(self,headA: Optional[ListNode],headB: Optional[ListNode]):
        if not headA or not headB:
            return None
        pa = headA
        pb = headB
        lenA = lenB = 0
        while pa:
            lenA += 1
            pa = pa.next
        while pb:
            lenB += 1
            pb = pb.next
        if lenB > lenA:
            tmp = headA
            headA = headB
            headB = tmp
            cur =lenA
            lenA = lenB
            lenB = cur
        pa = headA
        pb = headB
        for i in range(lenA - lenB):
            pa = pa.next
        while pa and pb:
            if pa == pb:
                return pa
            pa = pa.next
            pb = pb.next
        return None