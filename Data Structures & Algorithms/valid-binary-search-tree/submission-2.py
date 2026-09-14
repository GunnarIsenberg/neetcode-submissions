# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        #We should instead define a bounds of valid values. 
        def search(node, upper, lower):
            if node is None:
                return True

            elif node.val is not None and upper > node.val > lower: 
                return (search(node.left, node.val, lower) 
                    and search(node.right, upper, node.val))

            else:

                return False


        return search(root, float('inf'), float('-inf'))