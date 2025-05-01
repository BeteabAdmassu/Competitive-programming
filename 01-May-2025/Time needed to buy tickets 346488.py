# Problem: Time needed to buy tickets - https://leetcode.com/problems/time-needed-to-buy-tickets/

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        line = deque()
        n = len(tickets)
        time = 0
        for i in range(n):
            line.append(i)
        
        while tickets[k] != 0:
            tickets[line[0]] -= 1
            if len(line) > 1:
                buyer = line.popleft()
                if tickets[buyer] > 0:
                    line.append(buyer)
            time += 1
        return time