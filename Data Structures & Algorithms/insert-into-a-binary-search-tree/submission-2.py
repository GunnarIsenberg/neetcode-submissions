# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            node = TreeNode()
            node.val = val
            return node

        rt = self.findRoot(root, val)
        self.insert(rt, val)
        return root
    
    def findRoot(self, r : TreeNode, v:int):
        if r.val > v:
            if r.left == None:
                return r
            return self.findRoot(r.left, v)
        elif r.val < v:
            if r.right == None:
                return r
            return self.findRoot(r.right, v)
    
    def insert(self, r, v):
        node = TreeNode()
        node.val = v
        if r.val > v:
            r.left = node
        else:
            r.right = node
            

        