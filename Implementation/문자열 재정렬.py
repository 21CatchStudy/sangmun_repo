#문제 문자열 재정렬 
data = input()
result = []
value = 0

for x in data :
    if x.isalpha():
        result.append(x)

        else:
            value += int(x)

result.sort()


if value !=0:
    result.append(str(value))

print(''.join(result))


