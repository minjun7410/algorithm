import sys
input = sys.stdin.readline
a = input().rstrip()
b = input().rstrip()
stack = []
for c in a:
    stack.append(c)
    if c == b[-1] and len(stack) >= len(b) and ''.join(stack[-len(b):]) == b:
        for _ in range(len(b)):
            stack.pop()
if stack:
    print(''.join(stack))
else:
    print("FRULA")




