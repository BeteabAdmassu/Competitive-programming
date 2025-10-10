# Problem: Digit Operations to Make Two Integers Equal - https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/description/?envType=problem-list-v2&envId=shortest-path

prime = [True for _ in range(10001)]
factor = 2

while factor * factor <= 10001:
    if prime[factor]:
        for i in range(factor * factor, 10001, factor):
            prime[i] = False
    factor += 1
class Solution:
    def minOperations(self, n: int, m: int) -> int:
        if n == 1 and m == 1:
            return 1
        
        if prime[n]:
            return -1
        
        heap = []
        heapq.heappush(heap, (0, n))
        visited = set()

        while len(heap) > 0:
            cost, num = heapq.heappop(heap)

            if num == m:
                return cost + num
            
            if num in visited:
                continue
            
            visited.add(num)

            num_list = list(str(num))

            for i, digit in enumerate(num_list):
                num_copy = num_list[:]

                if digit == '9':
                    num_copy[i] = '8'
                    new_val = "".join(num_copy)

                    if not prime[int(new_val)] and new_val[0] != 0:
                        heapq.heappush(heap, (cost + num, int(new_val)))
                elif digit == '0':
                    num_copy[i] = '1'
                    new_val = "".join(num_copy)

                    if not prime[int(new_val)] and new_val[0] != 0:
                        heapq.heappush(heap, (cost + num, int(new_val)))
                else:
                    digit = int(digit)
                    num_copy[i] = str(digit - 1)
                    new_val = "".join(num_copy)

                    if not prime[int(new_val)] and new_val[0] != 0:
                        heapq.heappush(heap, (cost + num, int(new_val)))

                    num_copy[i] = str(digit + 1)
                    new_val = "".join(num_copy)

                    if not prime[int(new_val)] and new_val[0] != 0:
                        heapq.heappush(heap, (cost + num, int(new_val)))
        return -1

