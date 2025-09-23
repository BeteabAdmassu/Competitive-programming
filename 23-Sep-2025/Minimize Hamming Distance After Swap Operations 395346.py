# Problem: Minimize Hamming Distance After Swap Operations - https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/description/

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return 
        if rootX < rootY:
            self.parent[rootY] = rootX
        else:
            self.parent[rootX] = rootY


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        uf = UnionFind(len(source))
        for sw in allowedSwaps:
            a, b = sw
            uf.union(a, b)
        
        dict_track = defaultdict(list)
        for i in range(len(source)):
            dict_track[uf.find(i)].append(i)
        
        count = 0
        for ind in dict_track.values():
            count_src = Counter(source[i] for i in ind)
            count_tar = Counter(target[i] for i in ind)

            temp = sum(min(count_src[x], count_tar[x]) for x in count_src)
            count += len(ind) - temp
        
        return count
