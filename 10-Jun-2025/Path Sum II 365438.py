# Problem: Path Sum II - https://leetcode.com/problems/path-sum-ii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        
        def dfs(node, current_path, remaining_sum):
            if not node:
                return
            current_path.append(node.val)
            remaining_sum -= node.val
            if not node.left and not node.right and remaining_sum == 0:
                result.append(list(current_path))
            dfs(node.left, current_path, remaining_sum)
            dfs(node.right, current_path, remaining_sum)
            current_path.pop() 
        
        dfs(root, [], targetSum)
        return result
        