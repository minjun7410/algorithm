string = input()
tmp = ''
result = 0
is_miners = False
for i in string:
    if is_miners and (i == '+' or i == '-'):
        result -= int(tmp)
        tmp = ''
    elif i == '+' and not(is_miners):
        result += int(tmp)
        tmp = ''
    elif i == '-':
        is_miners = True
        result += int(tmp)
        tmp = ''
    else:
        tmp += i
if is_miners:
    result -= int(tmp)
else:
    result += int(tmp)
print(result)
