import sys
from collections import deque

direction = True  # True = left False = right


def R(dequeue):
    global direction
    direction = False if direction else True
    return dequeue


def D(dequeue):
    global direction
    if len(dequeue) == 0:
        return 'error'
    if direction:
        dequeue.popleft()
    else:
        dequeue.pop()
    return dequeue


T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    direction = True
    command = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    lst = deque(input().strip('[]\n').split(','))
    if lst[0] == '':
        lst = []
    for char in command:
        if char == 'R':
            result = R(lst)
        else:
            result = D(lst)
        if result == "error":
            break
    if result == "error":
        print('error')
    elif direction:
        print('[' + ','.join(result) + ']')
    else:
        print('[' + ','.join(reversed(result)) + ']')
    