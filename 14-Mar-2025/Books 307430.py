# Problem: Books - https://codeforces.com/contest/279/problem/B

n , t = map(int,input().split())
if n == 0 or t == 0:
    print(0)
    exit()
books = list(map(int,input().split()))


left = 0
count = 0 
_sum = 0
for i in range(n):
    _sum += books[i]
    while _sum > t:
        _sum -= books[left]
        left += 1
    count = max(count,i - left + 1)
print(count )