N = int(input())
result = 0
if N <= 99:
    result = N
else:
    result += 99
    for i in range(100, N+1):
        a = i % 10
        i = i / 10
        b = int(i) % 10
        i = i / 10
        c = int(i)
        if a - b == b - c:
            result += 1
print(result)