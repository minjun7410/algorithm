#dp

import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())

sequence = [[[-1 for _ in range(M+1)] for _ in range(M+1)] for _ in range(N+1)]
result = []
def recursion(length, temp_num, recent_num):
    if length > N or temp_num > M: return 0
    if sequence[length][temp_num][recent_num] != -1:
        return sequence[length][temp_num][recent_num] # 이미 지나갔던 곳은 먼저번에 계산한걸로 리턴
    sequence[length][temp_num][recent_num] = 0
    for i in range(recent_num, M+1):
        next_num = i + temp_num
        if next_num > M: break
        sequence[length][temp_num][recent_num] += recursion(length + 1, next_num, i)
    return sequence[length][temp_num][recent_num]
def trace(length, temp_num, recent_num, k):
    if length == N: return
    for i in range(recent_num, M+1):
        if sequence[length+1][temp_num+i][i] == -1: continue

        if sequence[length+1][temp_num+i][i] < k:
            k -= sequence[length+1][temp_num+i][i]
            continue
        result.append(i)

        trace(length+1, temp_num+i, i, k)
        break
for i in range(1, M+1):
    sequence[N][M][i] = 1

recursion(0,0,1)
trace(0,0,1,K)
print(' '.join(map(str, result)))


