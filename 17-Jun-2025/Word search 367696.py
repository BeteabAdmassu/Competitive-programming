# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        def dfs(i,j, l):
            if l == len(word):
                return True
            if i < 0 or j < 0:
                return False
            if i >= len(board) or j >= len(board[i]):
                return False
            if board[i][j] != word[l] or (i,j) in path:
                return False
            path.add((i,j))
            res = (dfs(i+1,j,l+1) or dfs(i,j+1,l+1) or
            dfs(i-1, j,l+1) or
            dfs(i, j-1, l+1))
            path.remove((i,j))
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True
        return False