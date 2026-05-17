# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 1
        i = head

        while i.next:
            l += 1
            i = i.next
        
        t = l - n

        if t == 0:
            return head.next

        j = 0
        prev = None
        nxt = head
        while j < t:
            prev = nxt
            nxt = nxt.next
            j += 1

        prev.next = nxt.next
        nxt.next = None
    
        return head
        