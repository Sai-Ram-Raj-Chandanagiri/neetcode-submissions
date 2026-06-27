# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBal = True

        def height(node):
            nonlocal isBal

            if not node:
                return 0
            leftheight = height(node.left)
            rightheight = height(node.right)

            if abs(leftheight - rightheight) >1:
                isBal = False
            
            return 1+ max(leftheight,rightheight)
        
        height(root)

        return isBal
        