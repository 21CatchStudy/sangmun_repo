
# https://www.acmicpc.net/problem/12865

n,k = map(int,input().split())
for i in range(n,k) :
    w,v = map(int,input().split())

d = [0] * 100
d[0] = w,v[0]
d[1] = max[w,v[1], w,v[2]]
for i in range(2,n) :
    d[i] = max(d[i - 1], d[i - 2] + w,v[i])
print(d[n - 1])
    

  ----------------------------------------------
import sys

N, K = map(int, input().split())
stuff = [[0,0]]
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    stuff.append(list(map(int, input().split())))


#냅색 문제 풀이
for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = stuff[i][0] 
        value = stuff[i][1]
       
        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j] #weight보다 작으면 위의 값을 그대로 가져온다
        else:
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

print(knapsack[N][K])
