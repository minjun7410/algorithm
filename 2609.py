a, b = map(int, input().split())
a, b = (b, a) if b > a else (a, b)
a1, b1 = a, b
r = 1
while r:  # 유클리드 호제법 or 유클리드 알고리즘 : a와 b를 나눈 나머지가 b가 되고  b가 a가 된다. 나머지가 0이 될때 b가 최대 공약수 
#{ 위키백과: 2개의 자연수(또는 정식) a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면(단, a>b), a와 b의 최대공약수는 b와 r의 최대공약수와 같다. 이 성질에 따라, b를 r로 나눈 나머지 r'를 구하고, 다시 r을 r'로 나눈 나머지를 구하는 과정을 반복하여 나머지가 0이 되었을 때 나누는 수가 a와 b의 최대공약수이다}
    r = a1 % b1
    a1 = b1
    b1 = r
print(a1)
print(a//a1 * b)  #두 정수를 최대공약수를 나눈 뒤 둘을 곱한후 최대공약수로 곱하면 최소공배수가 나옴