#https://www.acmicpc.net/problem/1654

import sys
input = sys.stdin.readline
k, n = map(int, input().split())
s = []
for i in range(k): s.append(int(input()))
low, high = 0, 10000000000
while low <= high:
    mid = (low + high) // 2
    num = 0
    for i in s: num += i // mid
    if num >= n: 
      low = mid + 1
    else: 
      high = mid - 1
print(high)
