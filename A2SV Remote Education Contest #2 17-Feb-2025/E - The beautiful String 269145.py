# Problem: E - The beautiful String - https://codeforces.com/gym/586622/problem/E


t = int(input().strip())


for _ in range(t):
    s = list(input().strip())
    q = int(input())
    hash_check = set()
    
    

    for i in range(len(s)):
        if s[i:i+4] == ["1","1","0","0"]:
            hash_check.add(i)
    

 
    for _ in range(q):
        i, v = map(int, input().split())
        i -= 1  

        s[i] = str(v)

        for j in range(max(0,i-3),min(i+1, len(s))):
            if s[j:j+4] == ["1", "1", "0", "0"]:
                hash_check.add(j)
            else:
                hash_check.discard(j)


        if len(hash_check) > 0:
            print("YES")
        else:
            print("NO")


