class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.size = 0
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        for i in range(index + 1):
            cur = cur.next
        return cur.val
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        index = max(0,index)
        self.size += 1
        pre = self.head
        for _ in range(index):
            pre = pre.next
        toAdd = ListNode(val)
        toAdd.next = pre.next
        pre.next = toAdd
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        self.size -= 1
        pre = self.head
        for _ in range(index):
            pre = pre.next
        pre.next = pre.next.next
class ListNode:
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = None

