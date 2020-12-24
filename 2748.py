
N = int(input())
stack = [0 for _ in range(N+1)]


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    if stack[n]:
        return stack[n]
    stack[n] = fibonacci(n-1) + fibonacci(n-2)
    return stack[n]


print(fibonacci(N))
