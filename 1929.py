import math
M, N = map(int, input().split())

def isPrime(M):
    lst = [True for _ in range(M+1)]
    for i in range(2, int(math.sqrt(M))+1):
        if lst[i]:
            j = 2
            while i*j <= M:
                lst[i*j] = False
                j += 1
    return lst

result = isPrime(N)

for i in range(1, len(result)):
    tmp = result[i]
    if not tmp or i == 1: #소수가 나온 경우, 1(소수가 아님)이 나온경우
        continue
    if i >= M and i <= N:
        print(i)
