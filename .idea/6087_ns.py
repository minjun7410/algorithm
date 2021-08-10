# BFS 문제
# 꺾는 수를 그래프에 저장한다.
# 진행할 때 현재 노드가 다음 진행 노드보다 수가 적어야 함

import sys

input = sys.stdin.readline

# input
W, H = map(int, input().split())
table = [[] for _ in range(H)]
start, end = None, None
for i in range(H):
	for j, tmp in enumerate(list(input().rstrip())):
		table[i].append(tmp)
		if tmp == 'C':
			start = (i, j) if start == None else start
			end = (i, j) if start != None or end != None else end


