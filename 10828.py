import sys
N = int(sys.stdin.readline().rstrip())
lst = []
for _ in range(N):
    command = sys.stdin.readline().rstrip().split()
    if command[0] == "push":
        lst.append(command[1])
    elif command[0] == "pop":
        if len(lst) == 0:
            print(-1)
            continue
        tmp = lst.pop()
        print(tmp)
    elif command[0] == "size":
        print(len(lst))
    elif command[0] == "empty":
        if len(lst) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "top":
        if len(lst) == 0:
            print(-1)
            continue
        else:
            print(lst[-1])
    else:
        print("error")
    