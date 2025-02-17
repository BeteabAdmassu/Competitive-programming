# Problem: B - Card Game - https://codeforces.com/gym/588094/problem/B

n = int(input())
cards = list(map(int, input().split()))


indexed_cards = [(cards[i], i + 1) for i in range(n)]


indexed_cards.sort()


for i in range(n // 2):
    print(indexed_cards[i][1], indexed_cards[n - 1 - i][1])