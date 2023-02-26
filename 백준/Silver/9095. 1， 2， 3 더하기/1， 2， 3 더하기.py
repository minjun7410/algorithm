import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    memoization = [0 for _ in range(n+1)]
    memoization[0] = 1
    for i in range(n):
        for j in [1, 2, 3]:
            if i + j <= n:
                memoization[i+j] += memoization[i]

    print(memoization[-1])