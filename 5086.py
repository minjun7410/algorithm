a, b = map(int, input().split())
while (a, b) != (0, 0):
    if not(b % a):
        print("factor")
    elif not(a % b):
        print("multiple")
    else:
        print("neither")
    a, b = map(int, input().split())