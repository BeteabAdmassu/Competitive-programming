# Problem: Partition String  - https://leetcode.com/problems/partition-string/description/

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        temp = self.root
        for c in word:
            i = ord(c) - 97
            if not temp.children[i]:
                temp.children[i] = TrieNode()
            temp = temp.children[i]
        temp.is_end = True

    def search(self, word):
        temp = self.root
        for c in word:
            i = ord(c) - 97
            if not temp.children[i]:
                return False
            temp = temp.children[i]
        return True if temp.is_end else False

    def partitionString(self, s: str) -> List[str]:
        found = set()
        res = []
        i = 0
        n = len(s)
        while i < n:
            j = i + 1
            while j <= n and self.search(s[i:j]):
                j += 1
            
            segment = s[i:j]
            if segment not in found:
                res.append(segment)
                found.add(segment)
            self.insert(segment)
            i = j
        return res