# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        ptr = l1
        num1 = ""
        while ptr is not None:
            num1 += (str(ptr.val))
            ptr = ptr.next

        ptr = l2
        num2 = ""
        while ptr is not None:
            num2 += (str(ptr.val))
            ptr = ptr.next
        
        num1 = num1[::-1]
        num2 = num2[::-1]
        solSum = int(num1) + int(num2)
        solSumStr = str(solSum)[::-1]

        dummy = ListNode()
        ptr = dummy
        for c in solSumStr:
            ptr.next = ListNode(int(c))
            ptr = ptr.next

        return dummy.next
        