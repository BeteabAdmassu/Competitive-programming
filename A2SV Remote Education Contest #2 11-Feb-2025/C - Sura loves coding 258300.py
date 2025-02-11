# Problem: C - Sura loves coding - https://codeforces.com/gym/586622/problem/C

enc_len = int(input())
enc_word = input()

res = []
for i, ch in enumerate(enc_word):
    if i % 2 == 0:
        res.append(ch)
    else:
        res.insert(0, ch)

if enc_len % 2 == 0:
    res.reverse()

print(''.join(res))