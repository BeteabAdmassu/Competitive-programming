# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedHash = {i for i in allowed}
        flag = False
        count = 0
        for word in words:
            wordSet = set(word)
            for char in wordSet:
                if char not in allowedHash:
                    flag = True

            if flag:
                flag = False
                continue
            count += 1

        return count


        