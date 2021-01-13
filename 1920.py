N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
B = list(map(int, input().split()))


def binary_search(n):
    MID = (len(A)-1) // 2
    LEFT = 0
    RIGHT = len(A) - 1
    while A[MID] != n:
        if RIGHT < LEFT :
            return 0
        if A[MID] > n:
            RIGHT = MID - 1
            MID = LEFT + (RIGHT - LEFT) // 2
        elif A[MID] < n:
            LEFT = MID + 1
            MID = LEFT + (RIGHT - LEFT) // 2
            
    return 1
    

for target in B:
    print(binary_search(target))
    