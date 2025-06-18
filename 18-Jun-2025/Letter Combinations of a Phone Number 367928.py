# Problem: Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        l = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        ans = []
        def solve(curr = 0, arr = []):
            if curr == len(digits): 
                if arr: ans.append(''.join(arr))
                return
            for c in l[digits[curr]]:
                arr.append(c)
                solve(curr + 1, arr)
                arr.pop()
        solve()
        return ans