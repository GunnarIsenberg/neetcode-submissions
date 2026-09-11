# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def helper(p, q):
            if p == None and q == None:
                return True
            elif (p == None and q != None) or (q == None and p != None):
                return False
            elif p.val != q.val:
                return False
            else : return helper(p.left, q.left) and helper(p.right, q.right)
        return helper(p, q)