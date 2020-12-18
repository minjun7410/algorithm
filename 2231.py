def brute_force(N):
    for j in range(0, N+1):
        i = j
        sums = i
        while i > 0:
            sums += i % 10
            i //= 10
        if sums == N:
            return j
N = int(input())
result = brute_force(N)
if not(result):
    print(0)
else:
    print(result)