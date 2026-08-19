# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        return self.helper(None, head)

    def helper(self, prev, cur):
        if cur.next is None:
            cur.next = prev
            return cur
        
        nxt = cur.next
        cur.next = prev
        
        return self.helper(cur, nxt)
        