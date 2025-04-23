# Problem: First Unique Character in a String - https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=problem-list-v2&envId=queue

class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_count = Counter(s)
        found = []
        for i in s_count:
            if s_count[i] == 1:
                found.append(s.find(i))
        return min(found) if len(found) > 0 else -1
        