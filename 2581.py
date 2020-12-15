import math

def isPrime(N):
    lst = [True for _ in range(N+1)]
    for i in range(2, int(math.sqrt(N)) + 1):
        if lst[i]:
            j = 2
            while i*j <= N:
                lst[i*j] = False
                j += 1
    return lst

M = int(input())
N = int(input())
lst = isPrime(N)
boolean = False
sums = 0
worst = None
for i in range(M, N+1):
    if i == 1:
        continue
    if not boolean and lst[i]:
        boolean = True
        worst = i
    if lst[i]:
        sums += i

if not worst:
    print(-1)
else:
    print(sums)
    print(worst)
