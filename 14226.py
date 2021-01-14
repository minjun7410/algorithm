from collections import deque
S = int(input())
dp = [[False for _ in range(S*2)] for _ in range(S * 2)]
queue = deque([(1, 0, 0)])  # (현재 화면 이모티콘 수, COPY count, result)
tmp = [0, 0]
while tmp[0] != S:
    tmp = queue.popleft()
    if dp[tmp[0]][tmp[1]]:
        continue
    elif tmp[0] <= 0 or tmp[0] > S + S//2:
        continue
    else:
        dp[tmp[0]][tmp[1]] = True
    if tmp[0] > S:
        que = deque([(tmp[0] - 1, tmp[1], tmp[2] + 1)])
    elif tmp[0] == tmp[1]:
        que = deque([(tmp[0] + tmp[1], tmp[1], tmp[2] + 1), (tmp[0] - 1, tmp[1], tmp[2] + 1)])
    else:
        que = deque([(tmp[0], tmp[0], tmp[2] + 1), (tmp[0] + tmp[1], tmp[1], tmp[2] + 1), (tmp[0] - 1, tmp[1], tmp[2] + 1)])
    queue = queue + que
print(tmp[2])