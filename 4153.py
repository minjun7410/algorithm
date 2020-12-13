while True:
    array = list(map(int, input().split()))
    array.sort()
    a, b, c = array
    if a + b + c == 0:
        break
    if a**2 + b**2 == c**2:
        print("right")
    else:
        print("wrong")