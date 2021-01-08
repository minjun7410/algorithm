stack = [0]  # push, pop을 진행할 리스트. 인자가 하나도 없을 떄를 대비하여 0을 넣음
result = []  # '+', '-' push, pop 진행 순서를 넣음
N = int(input())
rang = [i for i in range(1, N+1)][::-1]  # [1, 2, 3, 4, 5]
lst = [int(input()) for _ in range(N)]  # [5, 1, 3, 2, 4]
for value in lst: 
    if value == stack[-1]:  # 마지막 인자가 lst의 마지막 인자와 같을 때 pop
        stack.pop()
        result.append('-')
        continue
    elif value > stack[-1]:  # 마지막 인자가 value보다 작으면 그에 상응할 떄 까지 rang에서 꺼내서 push
        if len(rang) == 0:
            break
        else:
            tmp = None
            while tmp != value:  # 1. 스택의 마지막 인자를 value에 맞춘다.
                if len(rang) == 0:  # 2. 맞추지 못하고 더이상 넣을 숫자가 없을 경우 브레이크
                    break
                tmp = rang.pop()
                stack.append(tmp)
                result.append('+')
            if value == stack[-1]:  # 1. 맞춘다면 스택을 pop하고 while 계속 진행
                stack.pop()
                result.append('-')
                continue
            else:  # 못맞추고 비정상적으로 브레이크를 걸면 while에서 빠져나오고 if 문에서 "NO"를 프린트
                break
            
    elif value < stack[-1]:
        if len(stack) == 1:
            break
        tmp = stack.pop()
        result.append('-')
        continue
if stack[-1] == 0:
    for value in result:
        print(value)
else:
    print("NO")


