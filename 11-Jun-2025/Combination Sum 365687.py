# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
    
        def backtrack(start, current_combination, remaining_target):
            if remaining_target == 0:
                result.append(list(current_combination))
                return
            for i in range(start, len(candidates)):
                num = candidates[i]
                if num > remaining_target:
                    continue
                current_combination.append(num)
                backtrack(i, current_combination, remaining_target - num)
                current_combination.pop()
    
        candidates.sort()
        backtrack(0, [], target)
        return result
        