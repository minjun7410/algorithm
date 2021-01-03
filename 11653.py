import math
N = int(input())
prime = [True for _ in range(N+1)]
for index in range(2, int(math.sqrt(N))+1):
    if prime[index]:
        j = 2
        while index * j <= N:
            prime[index*j] = False
            j += 1
result = list(filter(lambda x: prime[x], range(2, N+1)))
if not(N == 1):
    for value in result:
        while N % value == 0:
            N //= value
            print(value)
            