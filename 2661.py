# 백트래킹, DFS 문제
# 처음엔 연속된 수열이 점화식을 가지는 줄 알았지만 숫자가 하나씩 갱신될 때마다
# 모든 수열이 겹치는 가를 조사해야하므로 DP는 탈락
# 게다가 입력받는 수가 80이하로 꽤 낮은 수이기 때문에 백트래킹, DFS를 사용했다.

import sys
input = sys.stdin.readline


def check_duplicates(seq):
    length = len(seq)
    for i in range(1, (length//2) + 1):
        boolean = True
        for j in range(1, i+1):
            if seq[-j] != seq[-(j+i)]:
                boolean = False
                break
        if boolean:
            return True
    return False


flag = False


def back_tracking(n, seq):
    global flag
    if n == N:
        flag = True
        return seq
    for cha in ['1', '2', '3']:
        tmp = seq + cha
        if check_duplicates(tmp):
            continue
        else:
            res = back_tracking(n+1, tmp)
            if flag:
                return res
    return seq


N = int(input())
result = back_tracking(1, '1')
print(int(result))