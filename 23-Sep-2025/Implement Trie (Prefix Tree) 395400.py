# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    def __init__(self):
        self.children = [None for x in range(26)]
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        temp = self.root
        for c in word:
            i = ord(c) - 97
            if not temp.children[i]:
                temp.children[i] = TrieNode()
            temp = temp.children[i]
        temp.is_end = True

    def search(self, word: str) -> bool:
        temp = self.root
        for c in word:
            i = ord(c) - 97
            if not temp.children[i]:
                return False
            temp = temp.children[i]
        return True if temp.is_end == True else False

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for c in prefix:
            i = ord(c) - 97
            if not temp.children[i]:
                return False
            temp = temp.children[i]
        return True
