# Problem: Remove Sub-Folders from the Filesystem - https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
    
    def add(self, path):
        temp = self
        for i in path.split("/"):
            if i not in temp.children:
                temp.children[i] = TrieNode()
            temp = temp.children[i]
        temp.is_end = True
    
    def prefix_search(self, path):
        temp = self
        folders = path.split("/")
        for i in range(len(folders) - 1):
            temp = temp.children[folders[i]]
            if temp.is_end:
                return True
        return False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = TrieNode()
        res = []
        
        for f in folder:
            trie.add(f)

        for f in folder:
            if not trie.prefix_search(f):
                res.append(f)
        return res