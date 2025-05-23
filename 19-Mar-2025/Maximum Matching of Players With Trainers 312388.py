# Problem: Maximum Matching of Players With Trainers - https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        left, right = 0 , 0
        count = 0

        while left < len(players) and right < len(trainers):
            if players[left] <= trainers[right]:
                count += 1
                left += 1
            right += 1

        return count