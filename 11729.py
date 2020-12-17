#하노이 탑
n = int(input())
lst = []
def hanoi(n, start, via, target):#옮겨야하는 탑의 층 수, 시작점, 경유지, 도착점을 지정
    if n == 1:#만약 n이 1이라면 경유지 없이 도착 가능
        lst.append(str(start) + ' ' + str(target))
        return
    hanoi(n-1, start, target, via)#첫번째 층을 제외한 모든 층을 경유지로 옮기고
    lst.append(str(start) + ' ' + str(target))#마지막 층을 도착지점으로 옮긴다
    hanoi(n-1, via, start, target)#그리고 경유지에 있는 모든 층을 도착점으로 옮긴다
    return

hanoi(n, 1, 2, 3)
print(len(lst))
for i in range(len(lst)):
    print(lst[i])