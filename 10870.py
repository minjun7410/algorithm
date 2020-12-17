N = int(input())
lst = [0 for _ in range(N+1)]
def fibonacci(n):
    if lst[n] != 0:
        return lst[n]
    if n == 1:
        lst[1] = 1
        return 1
    if n == 0:
        lst[0] = 0
        return 0
    lst[n] = fibonacci(n-1) + fibonacci(n-2)
    return lst[n]
print(fibonacci(N))