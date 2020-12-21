N = int(input())
result = 0
tmp = []
def dfs():
    global result
    if len(tmp) == N:
        result += 1
        return
    for i in range(N):
        if check(tmp, i):
            tmp.append(i)
            dfs()
            tmp.pop()


def check(tmp, i):
    for index, value in enumerate(tmp):
        height = len(tmp) - index
        if i == value:
            return False
        elif i + height == value or i - height == value:
            return False
        else:
            continue
    return True

dfs()
print(result)