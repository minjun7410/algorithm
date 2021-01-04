def gcd(num_1, num_2):
    num_1, num_2 = (num_1, num_2) if num_1 > num_2 else (num_2, num_1)
    if num_1 % num_2 == 0: 
        return num_2
    r = 1
    while r:
        r = num_1 % num_2
        num_1 = num_2
        num_2 = r
    return num_1


N = int(input())
lst = [int(input()) for _ in range(N)]
lst.sort(reverse = True)

diff = [a - b for a, b in zip(lst, lst[1:] + [0])][:-1]
tmp = diff[0]
for i in range(1, len(diff)):
    tmp = gcd(tmp, diff[i])
if len(diff) == 1:
    num_1, num_2 = (lst[0], lst[-1]) if lst[0] > lst[-1] else (lst[-1], lst[0])
    for i in range(num_2 - 1):
        if (num_1-i) % (num_2 - i) == 0:
            tmp = num_2 - i
            break
lst = []
for i in range(2, int(tmp ** (0.5)) + 1):
    if tmp % i == 0:
        lst.append(i)
        if tmp // i != i:
            lst.append(tmp // i)
lst.append(tmp)
print(' '.join(map(str, sorted(lst))))