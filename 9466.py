# dfs 문제
# 처음 학생이 결국에 마지막 학생이 처음 학생을 지목하면 팀 매치 성공이다.
# 지목한 학생의 지목 학생을 알아야하는 재귀적인 탐색을 이용해야함 -> dfs

# 1. 학생의 수 n이 주어지면 n+1개 리스트를 모두 True로 설정(True: 지목당하지 않음, False: 지목당함)
# 2. 1부터 n까지 반복문으로 dfs를 진행한다.
# 3. 초기 dfs함수를 호출할 때 인자로 (처음학생, 학생리스트)를 넘겨준다.
# 4. 만약 해당 학생이 지목한 학생 == 처음학생 이면 dfs 종료

# 참고: https://claude-u.tistory.com/435

# 후기
# 푸는데 너무 헷갈렸다. bfs 알고리즘을 많이 사용하다보니까 dfs를 신경 못썼던것이 크다.
# 당장 dfs문제를 풀어보도록 해야겠다.
# 그리고 recursion 에러때문에 recursionlimit을 늘렸는데
# 이렇게 재귀문을 사용하는 것보다 반복문으로 짜는것도 연습해야한다.
import sys
sys.setrecursionlimit(111111)
input = sys.stdin.readline

def dfs(i):
    global result
    visited[i] = True  # 현재 학생을 방문 처리, 평소 dfs문제처럼 방문처리하고 함수가 끝나면 방문처리를 철회하지 않아도 된다.
    # 그 이유는 이미 그 학생을 방문했다면 이후에 이 학생에게 볼일이 없음.
    cycle.append(i)  # 사이클 리스트에 i를 저장, 사이클 안에 있지 않아도 아래에 의해 걸러짐.
    if visited[students[i]]:
        if students[i] in cycle:  # 학생이 사이클 안에 있는지 검사 (이미 방문한 학생이 꼭 사이클에 있지 않음ㅁ)
            result += cycle[cycle.index(students[i]):]  # 처음으로 cycle에 있는 요소를 방문할 경우 사이클이 완성되었음을 의미한다.
            # 그때 처음 cycle에 방문한 그 노드부터 사이클이므로 cycle[cycle.index(students[i]):] 이게 최종 사이클 모형이다.
        return
    else:
        dfs(students[i])
for _ in range(int(input())):
    result = []
    n = int(input())
    students = [0] + list(map(int, input().split()))
    visited = [False for _ in range(n+1)]
    for i in range(1, n+1):  # 1부터 n+1까지 사이클이 있는지 dfs로 검사하는데 이미 그 학생을 방문했다면 dfs할 필요 없다.
        if visited[i]: continue
        cycle = []  # 사이클에 있는 요소를 저장하는 리스트
        dfs(i)
    print(n - len(result))