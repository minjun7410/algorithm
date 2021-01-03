T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    A1, B1 = (B, A) if B > A else (A, B)
    r = 999999
    while r:
        r = A1 % B1
        A1 = B1
        B1 = r
    print(A * B // A1)