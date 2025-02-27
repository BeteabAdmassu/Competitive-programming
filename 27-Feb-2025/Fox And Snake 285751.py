# Problem: Fox And Snake - https://codeforces.com/problemset/problem/510/A

col,  row = map(int,input().split())

rows = ['#'] * row
snake = ['.'] * row
snake[row - 1] = '#'
snakeR = ['.'] * row
snakeR[0] = '#'

flag = False
for i in range(col):
    if i % 2 == 0:
        print("".join(rows))
    else:
        if flag:
            print("".join(snakeR))
            flag = False
        else:
            print("".join(snake))
            flag = True