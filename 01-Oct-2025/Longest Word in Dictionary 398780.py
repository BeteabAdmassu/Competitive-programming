# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def longestWord(self, words: List[str]) -> str:
        
        def insert(self, word):
            cur = self.root

            for letter in word:
                if letter not in cur.children:
                    cur.children[letter] = TrieNode()
                cur = cur.children[letter]
            cur.end = True
        
        for word in words:
            insert(self, word)
        
        def search(self, word):
            cur = self.root
            result = False
            for letter in word:
                if cur.children[letter].end:
                    result = True
                else:
                    result = False
                    break
                cur = cur.children[letter]
            return result

        result = ''
        for word in words:
            if search(self, word):
                if len(result) == len(word):
                    result = min(word, result)
                result = max(result, word, key=len)
        
        return result