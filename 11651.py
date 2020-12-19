import sys
input = sys.stdin.readline
lst = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    lst.append((a, b))
lst.sort(key = lambda x: x[0])
lst.sort(key = lambda x: x[1])
for i in lst:
    print(' '.join(map(str, i)))