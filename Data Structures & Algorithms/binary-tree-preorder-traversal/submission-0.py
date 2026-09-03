# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def helper(node):
            if node is None:
                return
            res.append(node.val)
            if node.left == None and node.right == None:
                return
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
        
        helper(root)

        return res
            
        