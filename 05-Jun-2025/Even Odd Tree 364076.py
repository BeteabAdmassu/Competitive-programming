# Problem: Even Odd Tree - https://leetcode.com/problems/even-odd-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = deque([root])
        level = 0
        
        while queue:
            level_size = len(queue)
            prev_val = None
            
            for i in range(level_size):
                node = queue.popleft()
                if level % 2 == 0:
                    if node.val % 2 == 0:
                        return False
                    if prev_val is not None and node.val <= prev_val:
                        return False
                else:
                    if node.val % 2 != 0:
                        return False
                    if prev_val is not None and node.val >= prev_val:
                        return False
                
                prev_val = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            level += 1
        
        return True
        