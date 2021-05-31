# 에라토스테네스의 체
# 에라토스테네스의 체로 소수 판별한 후 start와 end를 투포인터?로 A+B을 구한다.
# 골드바흐의 추측: 2보다 큰 모든 짝수는 두 개의 소수 합으로 나타낼 수 있다.

# 두 소수의 합이 홀수가 되기 위해선 짝수 + 홀수 합이어야 하는데 짝수 소수는 오직 2만 존재하므로 A+B-2가 소수인지 확인하면 된다.
# https://codedrive.tistory.com/410

# 골드바흐와 홀수+짝수 = 홀수 공식을 몰라서 구글링을 했다. 소수 문제가 나오면 이런 원리들을 새겨야함
# 그리고 소수의 집합을 구할 때 최대 크기의 집합을 미리 구해놓는 것도 풀이에 좋을것 같다.
import sys
import math
input = sys.stdin.readline

def sieve(n):
    prime_numbers = [True for _ in range(n+1)]
    prime_numbers[0], prime_numbers[1] = False, False
    for num in range(2, int(math.sqrt(n)+1)):
        if not(prime_numbers[num]): continue
        times = 2
        while num * times <= n:
            prime_numbers[num*times] = False
            times += 1
    return prime_numbers

primes = sieve(2*10**6)
for _ in range(int(input())):
    A, B = map(int, input().split())
    if (A+B) % 2 == 0:  # 골드바흐의 추측
        if (A+B) == 2:
            result = False
        else:
            result = True
    else:
        result = True
        if A+B-2 < 2*10**6:
            if primes[A+B-2]:
                result = True
            else:
                result = False
        else:
            for prime in range(len(primes)):
                if not(primes[prime]):  continue
                if (A+B-2) % prime == 0:
                    result = False
                    break

    print("YES" if result else "NO")

