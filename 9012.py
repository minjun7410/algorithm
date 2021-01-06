
N = int(input())
for _ in range(N):
    lst = []
    string = input()
    result = "YES"
    for char in string:
        if char == "(":
            lst.append("(")
        else:
            if len(lst) == 0:
                result = "NO"
                break
            else:
                lst.pop()
    if len(lst) != 0:
        result = "NO"
    print(result)