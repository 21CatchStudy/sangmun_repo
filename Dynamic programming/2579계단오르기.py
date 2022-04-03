# https://www.acmicpc.net/problem/2579
n = int(input())
d = [0] * 100 
for i in range(1, n+1) :
    n_list = list(map(int(input().split())))
    d[i] = d[i-1] + 1


#규칙
    if d == 10 :
        d * 1
    elif d == 20 :
        d * 1
    elif d == 25 :
        d * 1
d[0] = n_list[0]
d[1] = max(n_list[0],n_list[1])
d[i] = max(d[i - 1])    

print(d[ n - 1])"""

---------------------------------------------

# https://www.acmicpc.net/problem/2579
# 계단은 한 번에 한 개 or 두 개
# 세 개 연속 X
# 마지막 무조건 도착


"""n = int(input())
stairs = [0] * (n + 1)
d = [0] * (n + 1)

for i in range(1, n + 1):
    stairs[i] = int(input())

  


if n == 1:
    print(stairs[n])

elif n == 2:
    print(stairs[1] + stairs[2])

else:
    d[1] = stairs[1]
    d[2] = stairs[1] + stairs[2]
    d[3] = max(stairs[2] + stairs[3], stairs[1] + stairs[3])


    for i in range(4, n+1):
        d[i] = max(d[i-3] + stairs[i] + stairs[i-1], d[i-2] + stairs[i])

    print(d)"
