# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        return self.reverse(None, head)
    
    def reverse(self, prev, nxt):
        if nxt.next:
            tmp = nxt.next
            nxt.next = prev
            return self.reverse(nxt, tmp)
        else:
            nxt.next = prev
            return nxt
            
        