import sys
A, B, C = map(int, sys.stdin.readline().split())
def divide_conquer(n, m):
    global C
    if m == 1:
        return n % C
    if m % 2 == 0:
        return (divide_conquer(n, m//2) **2 ) % C
    else:
        return ((n % C) * ((divide_conquer(n, m//2) ** 2) % C) ) % C
print(divide_conquer(A, B))
    