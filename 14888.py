from collections import deque
N = int(input())
number = list(map(int, input().split()))
numbers = deque(number)
max_num = -2000000000
min_num = 2000000000
# oper = ['+', '-', '*', '/']

# operators = [ j for i, j in enumerate(map(int, input().split())) if j != 0]
inputs = list(map(int, input().split()))
sums = sum(inputs)
operators = inputs[:]
tmp = []


def dfs():
    if len(tmp) == sums:
        numbers = deque(number)
        calculator(tmp, numbers)
        return

    for o in range(len(operators)):
        if operators[o] == 0:
            continue
        operators[o] -= 1
        tmp.append(o)
        dfs()
        operators[o] += 1
        tmp.pop()


def calculator(operator, numbers):
    global max_num, min_num
    tmp = numbers.popleft()
    for o in operator:
        next_tmp = numbers.popleft()
        if o == 0:
            tmp += next_tmp
        elif o == 1:
            tmp -= next_tmp
        elif o == 2:
            tmp *= next_tmp
        elif o == 3:
            if next_tmp*tmp >= 0:
                tmp //= next_tmp
            elif next_tmp < 0:
                tmp //= -(next_tmp)
                tmp *= -1
            elif tmp < 0:
                tmp = -(tmp) // next_tmp
                tmp = -(tmp)
            else:
                tmp //= next_tmp
    if tmp > max_num:
        max_num = tmp
    if tmp < min_num:
        min_num = tmp
    return
dfs()
print(max_num)
print(min_num)