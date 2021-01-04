def gcd(a, b):
    r = 1
    while r:
        r = (a % b)
        a = b
        b = r
    return a


N = int(input())
lst = list(map(int, input().split()))
for i in range(N):
    if i == 0:
        tmp = lst[i]
        continue
    target = lst[i]
    gcd_ = gcd(tmp, target)
    print(str(tmp // gcd_) + '/' + str(lst[i] // gcd_))