# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = None
        l = min(p.val, q.val)
        r = max(p.val, q.val)

        def dfs(node):
            if not node:
                return None
            if l <= node.val <= r:
                return node
            #In this case, node.val is either greater or less than both
            elif node.val <= l and node.val <= r:
                return dfs(node.right)
            else:
                return dfs(node.left)
        return dfs(root)
            
        