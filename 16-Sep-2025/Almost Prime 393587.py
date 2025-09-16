# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

def prime_sieve(n):
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = is_prime[1] = False
    i = 2
    while i * i <= n:
        if is_prime[i]:
            j = i * i
            while j <= n:
                is_prime[j] = False
                j += i
        i += 1
    return [i for i in range(2, n+1) if is_prime[i]]
def find_two(x):
    all_primes = prime_sieve(x)
    nums = set()
    n2 = len(all_primes)
    for i in range(n2):
        prime = all_primes[i]
        if prime * prime > x:
            break
        for j in range(i+1, n2):
            next_j = all_primes[j]
            if prime * next_j > x:
                break
            temp = prime
            while temp <= x:
                val = next_j
                while val * temp <= x:
                    nums.add(val * temp)
                    val *= next_j
                temp *= prime
    return len(nums)
if __name__ == "__main__":
    val = int(input())
    res = find_two(val)
    print(res)