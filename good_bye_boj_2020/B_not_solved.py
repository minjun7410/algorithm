def check(a, b):
    if (a, b) in visited:
        return visited[(a, b)]
    sums = 0
    for i in range(4):
        if lst[a][i] != lst[b][i]:
            sums += 1
    visited[(a, b)] = sums
    return sums



T = int(input())
for _ in range(T):
    N = int(input())
    lst = list(input().split())
    min_sum = 100000000
    visited = {}
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1, N):
                result = check(i, j) + check(j, k) + check(i, k)
                if result < min_sum:
                    min_sum = result
    print(min_sum)