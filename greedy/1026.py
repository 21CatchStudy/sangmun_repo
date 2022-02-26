# https://www.acmicpc.net/problem/1026

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort(reverse=True)
b.sort()


answer = 0
cnt = 0

for j in a :
    answer += j * b #a = a+b 를 의미함
    cnt += 1

print(answer)


# answer += a * b[cnt] #a = a+b 를 의미함
# TypeError: unsupported operand type(s) for +=: 'int' and 'list'
