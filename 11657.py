# 벨만-포드 알고리즘
# 출발 노드에서 모든 노드까지의 최대 거리를 구하나, 가중치가 음수가 있을 경우 ->
# 벨만-포드
# 이 알고리즘은 (간선-1)만큼 edge relaxation을 진행한다.
# edge relaxation이란 모든 간선 이동을 진행시키는 것이다.
# 이것을 (간선-1)만큼 진행하게 되면 적어도 출발지점으로부터 모든 경로의 경우의 수를 따지게 된다.
# 주의할 점은 negative cycle 이다.
# negative cycle은 같은 경로를 돌면 돌수록 이동거리가 줄어들게 되는 cycle인데
# 현재까지 (간선-1)만큼 edge relaxation을 진행했다면 마지막으로 한번더 진행했을 떄 하나라도 정점의 값이 바뀐다면 FALSE(답이 나오지 않는다.).
#https://ratsgo.github.io/data%20structure&algorithm/2017/11/27/bellmanford/
#https://m.blog.naver.com/kks227/220796963742

import sys
input = sys.stdin.readline
INF = 987654321

# input
N, M = map(int, input().split())
vertexs = [tuple(map(int, input().split())) for _ in range(M)] #(시작, 도착, 가중치)
visited = [INF for _ in range(N+1)]
visited[1] = 0
boolean = True  # negative cycle(무한대로 줄어드는 사이클)이 나올 때 False

def bellman_ford():
    for i in range(M):
        edge_relaxation(i)

def edge_relaxation(i):
    global boolean
    for s, e, w in vertexs:
        if visited[e] > visited[s] + w and visited[s] != INF: # 오른쪽 조건문처럼 INF가 나왔을 땐 걸러야함
            if i == M-1:
                boolean = False
                return
            visited[e] = visited[s] + w
bellman_ford()

# print 
if boolean == False:  # negative cycle
    print(-1)
else:
    for i in range(2, N+1):
        print(visited[i] if visited[i] != INF else -1)

# 시작 노드로부터 주어지는 모든 경로를 지나야 하기 때문에 (간선-1)번 edge relaxation을 하면 된다는것을 명심해야 할듯
# 노드(E) 간선(V)라고 치면 복잡도는 O(VE)