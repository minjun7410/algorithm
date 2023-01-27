from collections import deque
import sys
input = sys.stdin.readline

left = deque(list(input().rstrip()))
right = deque([])
for _ in range(int(input())):
    a = input().rstrip().split()
    if a[0] == 'P':
        left.append(a[1])
    elif a[0] == 'B':
        if left:
            left.pop()
    elif a[0] == 'L':
        if left:
            right.appendleft(left.pop())
    elif a[0] == 'D':
        if len(right) != 0:
            left.append(right.popleft())

print("".join(left+right))