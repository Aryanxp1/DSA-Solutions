class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        dummy = ListNode(-1)
        dummy.next = head
        ptr1 = dummy
        ptr2 = head
        if not head or not head.next:
            return head
        ptr3 = head.next
        while ptr2 and ptr3:
            ptr2.next = ptr3.next
            ptr3.next = ptr2
            ptr1.next = ptr3
            if ptr2.next:
                ptr3 = ptr2.next.next
            else:
                break
            ptr1 = ptr2
            ptr2 = ptr2.next
        return dummy.next
