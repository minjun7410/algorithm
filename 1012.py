from collections import deque

T = int(input())

dx = [-1, 1, 0, 0]        
dy = [0, 0, -1, 1]

def bfs(y, x):
    if graph[y][x] != 1:#접근한 노드가 이미 접근, 0일때
        return False
    
    visit_need = deque()
    visit_need.append((x, y))#가장 처음 접근하는 노드
    while visit_need:#인접한 노드가 없을 때 중지
        x, y = visit_need.popleft()
        if graph[y][x] == 1:#접근한 노드의 값이 1일 때
            graph[y][x] = 2#접근 표시
            for i in range(4):#상, 하 , 좌, 우 노드를 조사 
                nx = x + dx[i]
                ny = y + dy[i]
                if nx <= -1 or ny <= -1 or nx >= M or ny >= N:#범위에 준하지 않을 때 
                    continue
                visit_need.append((nx, ny))
    return True        
            
            

for _ in range(T):
    result = 0
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]#표 만들기
    for _ in range(K):#입력받아서 1의 위치에 넣어주기
        X, Y = map(int, input().split())
        graph[Y][X] = 1
    for i in range(N):
        for j in range(M):#하나하나 조사, 
            if bfs( i, j) == True:#bfs로 인접한 노드 모두 2로 표시 후 정답에 1 추가 
                result += 1
    print(result)
