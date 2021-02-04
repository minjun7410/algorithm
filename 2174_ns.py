# 구현 문제

# https://rebas.kr/739  참고
# 참고하고 짠 코드 (이래도 3%에서 틀림)
import sys
input = sys.stdin.readline


A, B = map(int, input().split())
N, M = map(int, input().split())
direction = {'S': 0, 'E': 1, 'N': 2, 'W': 3} 
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
w = [[0]*(A+1) for _ in range(B+1)]  # 맵
robots = [[0, 0, 0] for _ in range(N+1)]  # 로봇의 정보가 들어있는 리스트


def solve(robot_index, command, count):
    x, y, z = robots[robot_index]
    w[x][y] = 0  # 이동하기 전 자리 비우기
    for _ in range(count):
        if command == 'L':
            z = (z+1) % 4
        elif command == 'R':
            z = (z+3) % 4
        else:
            x, y = x + dx[z], y + dy[z]  # 이동
            if x < 1 or x > B or y < 1 or y > A:  # 벗어난 경우
                print("Robot %d crashes into the wall" % robot_index)
                return True
            if w[x][y]:  # 이동한 자리에 로봇이 있을 경우
                print("Robot %d crashes into robot %d" % (robot_index, w[x][y]))
                return True
    robots[i] = x, y, z
    w[x][y] = robot_index  # 이동 후 자리 매김
    return False
    
for i in range(1, N+1):
    x, y, z = input().split()
    w[int(y)][int(x)] = i
    robots[i] = [int(y), int(x), direction[z]]
flag = False
for _ in range(M):
    robot_index, command, count = input().split()
    if not flag:
        flag = solve(int(robot_index), command, int(count))
if not flag:
    print("OK")
''' [참고 x] 내가 짠 코드 (3%에서 틀림)
def change_direction(direct, count, present):
    if direct == 'R':
        present -= count
        present %= 4
        return present
    else:
        present += count
        present %= 4
        return present


def front(robot, count, number):
    global A, B
    direct_x, direct_y = direction[robot[2]][0], direction[robot[2]][1]
    for _ in range(count):
        robot[0] += direct_x
        robot[1] += direct_y
        if robot[0] < 1 or robot[0] > A or robot[1] < 1 or robot[1] > B:
            return "Robot " + str(number+1) + " crashes into the wall"
        for index, value in enumerate(robots):
            if index == number:
                continue
            if value[0] == robot[0] and value[1] == robot[1]:
                return "Robot " + str(number+1) + " crashes into robot " + str(index + 1)
    return "OK"


A, B = map(int, sys.stdin.readline().split())
N, M = map(int, sys.stdin.readline().split())
robots = []
for _ in range(N):
    x, y, direct = sys.stdin.readline().split()
    x, y = map(int, [x, y])
    if direct == 'E':
        robots.append([x, y, 1])
    elif direct == 'W':
        robots.append([x, y, 3])
    elif direct == 'S':
        robots.append([x, y, 2])
    else:
        robots.append([x, y, 0])
result = "OK"
for _ in range(M):
    robot, command, count = input().split()
    if result != "OK":
        continue
    robot, count = map(int, [robot, count])
    robot -= 1
    if command != 'F':
        direct = change_direction(command, count, robots[robot][2])
        robots[robot][2] = direct
    else:
        result = front(robots[robot], count, robot)
    print(robots)
print(result)'''