# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY  

        n = len(s)
        parent = list(range(n))  
        
        for a, b in pairs:
            union(a, b)
        
        components = {}
        for i in range(n):
            root = find(i)
            if root not in components:
                components[root] = []
            components[root].append(i)
        
        s = list(s) 
        for indices in components.values():

            chars = [s[i] for i in indices]
            chars.sort()  
            for i, idx in enumerate(sorted(indices)):
                s[idx] = chars[i]
        
        return ''.join(s)
