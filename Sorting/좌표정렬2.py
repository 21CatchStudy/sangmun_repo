#https://www.acmicpc.net/problem/11651 

import sys
n = int(sys.stdin.readline())
b = []
for i in range(n):
    b.append(list(map(int, sys.stdin.readline().split())))
b.sort(key=lambda x: (x[1], x[0]))

for i in b:
    print(i[0],i[1])    
