# dfs 문제
# 처음 학생이 결국에 마지막 학생이 처음 학생을 지목하면 팀 매치 성공이다.
# 지목한 학생의 지목 학생을 알아야하는 재귀적인 탐색을 이용해야함 -> dfs

# 1. 학생의 수 n이 주어지면 n+1개 리스트를 모두 True로 설정(True: 지목당하지 않음, False: 지목당함)
# 2. 1부터 n까지 반복문으로 dfs를 진행한다.
# 3. 초기 dfs함수를 호출할 때 인자로 (처음학생, 학생리스트)를 넘겨준다.
# 4. 만약 해당 학생이 지목한 학생 == 처음학생 이면 dfs 종료

import sys
from collections import deque
input = sys.stdin.readline

def dfs(visited, start):
    global flag
    queue = deque([start])
    while queue:
        temp = queue.pop()
        if not(visited[temp]): continue
        visited[temp] = False
        if start == temp: return
        queue.extend(students[temp])
        ####
    return

for _ in range(int(input())):
    n = int(input())
    students = [[] for _ in range(n+1)]
    for index, student in enumerate(map(int, input().split())):
        students[student].append(index+1)
    visited = [True for _ in range(n+1)]
    for i in range(1, n+1):
        if not(visited[i]): continue
        flag = False
        dfs(visited, i)
    print(visited.count(True)-1)