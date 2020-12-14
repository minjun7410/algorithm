import math
def isPrime(n): #에라토스테네스의 체
    numbers = [True for _ in range(n+1)]
    for i in range(2, int(math.sqrt(n))+1):
        if numbers[i]:
            j = 2
            while i * j <= n:
                numbers[i*j] = False
                j += 1
    return [i for i in numbers if i]
while True:
    N = int(input())
    if N == 0:
        break
    result = isPrime(N)
    print(result)