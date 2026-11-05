"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeMap = {}

        ptr = head
        if head is not None:
            while ptr is not None:
                newNode = Node(ptr.val, None, None)
                nodeMap[ptr] = newNode
                ptr = ptr.next

            ptr=head
            while ptr is not None:
                curNode = nodeMap[ptr]

                nxtNode = nodeMap.get(ptr.next)
                rndNode = nodeMap.get(ptr.random)

                curNode.next = nxtNode
                curNode.random = rndNode
                ptr = ptr.next
            return nodeMap[head]
        return head 
        