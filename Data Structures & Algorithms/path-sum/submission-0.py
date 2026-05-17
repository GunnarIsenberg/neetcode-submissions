# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, val):
            if not root:
                return False
            
            val += root.val 

            if not root.left and not root.right and val == targetSum:
                return True
            
            return(dfs(root.left, val) or dfs(root.right, val))

        return dfs(root, 0) 