# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        players = [i for i in range(1, n + 1)]

        _index = 0

        []

        while len(players) > 1:
            _index = (_index + (k -1) ) % len(players)
            print(_index)

            players.pop(_index)


        return players[0]


