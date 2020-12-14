r1 = int(input())
r2 = int(input())
r3 = 0
for i in range(3):
    tmp = int(r2) % 10
    print(tmp * r1)
    r3 += tmp * r1 * (10 ** i)
    r2 /= 10
print(r3)