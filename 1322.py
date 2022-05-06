# X와 Y
# 5 2
# 5+2 = 7 : 111
# 101 | 010 : 111
# 둘 다 비트가 겹치지 않아야 조건이 성립함.
from collections import deque


X, K = map(int, input().split())
X_bin = "0"*32 + bin(X)[2:]
K_bin = "0"*32 + bin(K)[2:]
result = deque([])
for x in reversed(list(X_bin)):
    if x == "1":
        result.appendleft(0)
    elif not(K_bin): break
    else:
        result.appendleft(0 if K_bin[-1] == '0' else 1)
        K_bin = K_bin[:-1]

print(int('0b'+''.join(list(map(str, result))), 2))