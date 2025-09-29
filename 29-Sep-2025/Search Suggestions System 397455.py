# Problem: Search Suggestions System - https://leetcode.com/problems/search-suggestions-system/

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False
        self.suggestions = []
class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        temp = self.root
        for c in word:
            i = ord(c) - 97
            if not temp.children[i]:
                temp.children[i] = TrieNode()
                temp.children[i].suggestions = []
            temp = temp.children[i]
            if len(temp.suggestions) < 3:
                temp.suggestions.append(word)
        temp.is_end = True

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        for word in products:
            self.insert(word)
        
        res = []
        temp = self.root
        for x in range(len(searchWord)):
            i = ord(searchWord[x]) - 97
            if temp.children[i]:
                temp = temp.children[i]
                res.append(temp.suggestions)
            else:
                res.extend([] for _ in range(x, len(searchWord)))
                break
                
        return res

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False
        self.suggestions = []
class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        temp = self.root
        for c in word:
            i = ord(c) - 97
            if not temp.children[i]:
                temp.children[i] = TrieNode()
                temp.children[i].suggestions = []
            temp = temp.children[i]
            if len(temp.suggestions) < 3:
                temp.suggestions.append(word)
        temp.is_end = True

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        for word in products:
            self.insert(word)
        
        res = []
        temp = self.root
        for x in range(len(searchWord)):
            i = ord(searchWord[x]) - 97
            if temp.children[i]:
                temp = temp.children[i]
                res.append(temp.suggestions)
            else:
                res.extend([] for _ in range(x, len(searchWord)))
                break
                
        return res

