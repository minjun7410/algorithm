import sys

K = int(sys.stdin.readline().rstrip())
lst = []
for _ in range(K):
    tmp = int(sys.stdin.readline().rstrip())
    if tmp != 0:
        lst.append(tmp)
    else:
        lst.pop()
print(sum(lst))