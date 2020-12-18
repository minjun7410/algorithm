def brute_force():
    global diff, result
    for i in lst:
        for j in lst:
            if j == i: continue
            for k in lst:
                if k == i or k == j: continue
                sums = (i + j + k)
                if sums == M:
                    result = M
                    return
                if sums <= M and M - sums < diff:
                    result = sums
                    diff = M - sums
        lst.remove(i)
N, M = map(int, input().split())
lst = list(map(int, input().split()))
result = 0
diff = M
brute_force()
print(result)