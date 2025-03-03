# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        output = [""] * len(s)

        for i in range(len(s)):
            output[indices[i]] = s[i]

        return "".join(output)
        