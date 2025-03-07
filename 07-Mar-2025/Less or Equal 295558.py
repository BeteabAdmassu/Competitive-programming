# Problem: Less or Equal - https://codeforces.com/problemset/problem/977/C

n,k = input().split()
n = int(n)
k = int(k)


array = list(map(int,input().split()))
array.sort()



if k == 0:
    if array[0] == 1:
        print(-1)
    else:
        print(1)
elif k == n or array[k-1] != array[k]:
    print(array[k-1])
else:
    print(-1)