# Problem: D - Mugisho and Rufeyda - https://codeforces.com/gym/586622/problem/D

n , t = map(int, input().split())
init = 10 ** (n - 1)

ans = init + (t - (init % t))

if ans < 10 ** n:
    print(ans)
else:
    print(-1)


