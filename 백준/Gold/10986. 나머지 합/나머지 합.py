import sys
from collections import Counter
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
sums = [A[0]%M]
for i in range(1, N):
    sums.append((A[i] + sums[i-1])%M)
counts = Counter(sums)
result = counts[0]
for c in counts.values():
    result += c*(c-1)//2
print(result)