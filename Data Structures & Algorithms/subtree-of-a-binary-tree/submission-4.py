# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = collections.deque()

        q.append(root)

        while q:
            node = q.popleft()
            
            if node is None:
                continue

            else:
                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)

                if node.val == subRoot.val:
                    if self.compareSubTree(node, subRoot):
                        return True
        return False
            
    def compareSubTree(self, l, r):
        if l is None and r is None:
            return True
        elif (l is None or r is None) or l.val != r.val:
            return False
        else:
            return self.compareSubTree(l.left, r.left) and self.compareSubTree(l.right, r.right)
