# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        root = [i for i in range(len(stones))]
        line = {}
        col = {}
        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]

        for i, (x, y) in enumerate(stones):
            if x not in col:
                col[x] = i
            if y not in line:
                line[y] = i
            root[find(i)] = find(col[x])
            root[find(i)] = find(line[y])
        ans = 0
        seen = set()
        for r in root:
            num = find(r)
            if num in seen: ans += 1
            else: seen.add(num)
        return ans