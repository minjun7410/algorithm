import sys
from collections import deque


def push_front(number):
    dequeue.appendleft(number)
    return


def push_back(number):
    dequeue.append(number)
    return


def pop_front():
    if len(dequeue) == 0:
        return -1
    tmp = dequeue.popleft()
    return tmp


def pop_back():
    if len(dequeue) == 0:
        return -1
    tmp = dequeue.pop()
    return tmp


def size():
    tmp = len(dequeue)
    return tmp


def empty():
    if len(dequeue) == 0:
        return 1
    else:
        return 0


def front():
    if len(dequeue) == 0:
        return -1
    else:
        return dequeue[0]


def back():
    if len(dequeue) == 0:
        return -1
    else:
        return dequeue[-1]


N = int(sys.stdin.readline().rstrip())
dequeue = deque([])
for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "push_back":
        push_back(command[1])
    elif command[0] == "push_front":
        push_front(command[1])
    elif command[0] == "pop_front":
        print(pop_front())
    elif command[0] == "pop_back":
        print(pop_back())
    elif command[0] == "size":
        print(size())
    elif command[0] == "empty":
        print(empty())
    elif command[0] == "front":
        print(front())
    elif command[0] == "back":
        print(back())
