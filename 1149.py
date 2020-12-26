N = int(input())
street_RGB = [[] for _ in range(N)]

for n in range(N):
    street_RGB[n] = list(map(int, input().split()))

street_min = [[] for _ in range(N)]
street_min[0] = street_RGB[0][:]
for i in range(1, N):
    for j, rgb in enumerate(street_RGB[i]):
        miner = 10000000
        for k, rgb_min in enumerate(street_min[i-1]):
            if k == j:
                continue
            if miner > rgb_min:
                miner = rgb_min
        street_min[i].append(rgb + miner)
print(min(street_min[N-1]))
        