# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        candidates = []

        def search(node, target):
            if node is None:
                return
            if node.val == target.val:
                candidates.append(node)
            search(node.left, target)
            search(node.right, target)
            
        def compare(n1, n2):
            if n1 is None and n2 is None:
                return True
            if ((n1 == None and n2 != None) 
                or (n1 != None and n2 == None) 
                or (n1.val != n2.val)):
                return False
            else:
                return compare(n1.left, n2.left) and compare(n1.right, n2.right)

        search(root, subRoot)

        for candidate in candidates:
            if compare(candidate, subRoot):
                return True
        return False
                
        
        