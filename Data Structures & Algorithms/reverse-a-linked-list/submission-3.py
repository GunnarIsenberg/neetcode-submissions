# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        p, c = None, head
        return self.swapWindow(p, c)
        
    def swapWindow(self, prev, curr):
        if curr.next:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        else:
            curr.next = prev
            return curr
        return self.swapWindow(prev, curr)