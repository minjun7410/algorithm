# 벨만-포드 알고리즘
# 출발 노드에서 모든 노드까지의 최대 거리를 구하나, 가중치가 음수가 있을 경우 ->
# 벨만-포드
# 이 알고리즘은 (간선-1)만큼 edge relaxation을 진행한다.
# edge relaxation이란 모든 간선 이동을 진행시키는 것이다.
# 이것을 (간선-1)만큼 진행하게 되면 적어도 출발지점으로부터 모든 경로의 경우의 수를 따지게 된다.
# 주의할 점은 negative cycle 이다.
# negative cycle은 같은 경로를 돌면 돌수록 이동거리가 줄어들게 되는 cycle인데
# 현재까지 (간선-1)만큼 edge relaxation을 진행했다면 마지막으로 한번더 진행했을 떄 하나라도 정점의 값이 바뀐다면 FALSE.
#https://ratsgo.github.io/data%20structure&algorithm/2017/11/27/bellmanford/
#https://m.blog.naver.com/kks227/220796963742