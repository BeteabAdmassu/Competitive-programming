# Problem: Merge Two Binary Trees - https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1

        stack = [(root1, root2)]

        while stack:
            a , b = stack.pop()

            a.val += b.val

            if a.left and b.left:
                stack.append((a.left,b.left))
            elif not a.left and b.left:
                a.left = b.left



            if a.right and b.right:
                stack.append((a.right, b.right))
            elif not a.right and b.right: 
                a.right = b.right

        return root1
        