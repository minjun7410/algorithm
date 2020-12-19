N = int(input())
lst = []
dic = {}
index = 0 #빈도수 구하기
for _ in range(N):
    tmp = int(input())
    lst.append(tmp)
    if tmp not in dic.keys():#한번도 카운트 하지 않은 수
        dic[tmp] = 1
        if index < dic[tmp]:#최빈값의 빈도수 구하기
            index = dic[tmp]
    else:
        dic[tmp] += 1
        if index < dic[tmp]:#최빈값의 빈도수 구하기
            index = dic[tmp]
many = [key for key, value in dic.items() if value == index]#최빈값의 빈도수를 가진 값만 리스트에 저장
lst.sort()
many.sort()#최빈값들을 정렬
#1
print(int(round(sum(lst)/N, 0)))
#2
print(lst[N//2])
#3
if len(many) == 1:
    print(many[0])
else:
    print(many[1])
#4
print(lst[-1] - lst[0])

