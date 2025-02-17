# Problem: D - Adjacents, ewww ! - https://codeforces.com/gym/588094/problem/D

t = int(input())
for _ in range(t):
    n = int(input())
    
    if n == 2:
        print(-1)
        continue
    
    if n == 1:
        print(1)
        continue
    
    nums = [x+1 for x in range(n**2)]
    
   
    result = [[] for _ in range(n)]
    for i in range(n):
        result[i] = []

    r = c = 0

    for i in range(0, len(nums), 2):
        result[r].append(nums[i])
        c += 1
        if c == n:
            c = 0
            r += 1


   
    for i in range(1, len(nums), 2):
        result[r].append(nums[i])
        c += 1
        if c == n:
            c = 0
            r += 1

    
    for row in result:
        print(*row)