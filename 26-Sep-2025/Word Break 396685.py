# Problem: Word Break - https://leetcode.com/problems/word-break/description/

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

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        for word in wordDict:
            self.insert(word)

        can_build = {0}
        queue = deque([0])
        while queue:
            i = queue.popleft()
            temp = self.root
            for j in range(i, len(s)):
                c = s[j]
                ind = ord(c) - 97
                if temp.children[ind]:
                    temp = temp.children[ind]
                    if temp.is_end and (j + 1) not in can_build:
                        can_build.add(j + 1)
                        queue.append(j + 1)
                else:
                    break
        return len(s) in can_build