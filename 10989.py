import sys
input = sys.stdin.readline
N = int(input())
count = [0 for _ in range(10000 + 1)]
for _ in range(N):
    count[int(input())] += 1
for i in range(1, 10000 + 1):
    for _ in range(count[i]):
        print(i) 