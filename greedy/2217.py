#https://www.acmicpc.net/problem/2217

import sys
input = sys.stdin.readline
n = int(input())
s = []
for i in range(n):
    s.append(int(input()))
s.sort(reverse=True)
max_n = 0
for i in range(n):
    if s[i] * (i + 1) > max_n:
        max_n = s[i] * (i + 1)
print(max_n)
