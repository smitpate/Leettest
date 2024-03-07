class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fst = head
        slw = head
        if not head:
            return None
        else:
            while fst and fst.next:
                fst = fst.next.next
                slw = slw.next
            return slw
