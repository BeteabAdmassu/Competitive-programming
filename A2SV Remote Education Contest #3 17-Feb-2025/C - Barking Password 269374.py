# Problem: C - Barking Password - https://codeforces.com/gym/588094/problem/C

password = input().strip()

N = int(input())

words = [0] * N

foundFlag = False
for i in range(N):
    word = input().strip()
    if word == password:
        foundFlag = True
        break
    else:
        words[i] = word
if foundFlag:
    print("YES")

if not foundFlag :

    first_char_match = False
    second_char_match = False

    for word in words:
        if word[1] == password[0]:
            first_char_match = True
        if word[0] == password[1]:
            second_char_match = True
    if first_char_match and second_char_match:
        print("YES")
    else:
        print("NO")



