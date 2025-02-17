# Problem: A - Nathan is rich - https://codeforces.com/gym/588094/problem/A

N = int(input())

for _ in range(N):
    _input = int(input())
    if _input ==2:
        print("1")
    else:
        q = _input // 4
        r = _input % 4

        if r != 0:
            q += 1
        print(q)