# 에라토스테네스, 투포인터
# 에라토스테네스의 체로 소수판별
# 찾은 소수 n를 반복문으로 2부터 n까지(단 소수만) 더한 값을 인덱스로 dp에 카운트한다.
# AC 그러나 시간이 간당하게 초과하지 않았다.
# 그리고 문제의 의도는 소수 판별 후, 투 포인터로 입력값을 나타내는 부분합을 구하는 것이었따.

# 따라서 투포인트 숙지 후 다시 풀어보았다.

# 요령은 간단한 것 같다.
# 처음 시작, 끝 인덱스를 0으로 지정하고 구하려는 수 N보다 작다면 end를 늘리고 sum을 증가시키고 크다면 start를 늘리고 sum을 감소시킨다.
# 이때 구하려는 수와 같다면 +1을 한다음 start를 증가시킨다.

# 구현하는데 인덱스가 너무 헷갈리고 index 에러가 많이 났다.

import math
import sys
input = sys.stdin.readline

def sieve(N):
    prime_numbers = [True for _ in range(N+1)]
    prime_numbers[0] = False
    prime_numbers[1] = False
    for number in range(2, int(math.sqrt(N))+1):
        if not(prime_numbers[number]): continue
        multi = 2
        while number * multi <= N:
            prime_numbers[number * multi] = False
            multi += 1
    primes = [prime for prime in range(N+1) if prime_numbers[prime]]
    return primes


N = int(input())
dp = [0 for _ in range(N+1)]
prime_numbers = sieve(N)
'''
for i in range(len(prime_numbers)):
    sums = 0
    for j in range(i+1):
        sums += prime_numbers[i-j]
        if sums > N: break
        dp[sums] += 1'''
# two pointer
result = 0
start, end, sums = 0, 0, 0
prime_numbers += [0]
while end < len(prime_numbers):
    if sums < N:
        sums += prime_numbers[end]
        end += 1
    elif sums >= N:
        sums -= prime_numbers[start]
        start += 1
    if sums == N:
        result += 1
print(result)



