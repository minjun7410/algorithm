# 구현 문제

direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # 북 동 남 서


def change_direction(direct, count, present):
    if direct == 'R':
        present -= count
        present %= 4
        return direction[present]
    else:
        present += count
        present %= 4
        return direction[present]


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


A, B = map(int, input().split())
N, M = map(int, input().split())
robots = []
for _ in range(N):
    x, y, direct = input().split()
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
    robot, count = map(int, [robot, count])
    robot -= 1
    if command != 'F':
        direct = change_direction(command, count, robots[robot][2])
        robots[robot][2] = direct
    else:
        result = front(robots[robot], count, robot)
        if result != "OK":
            break
print(result)