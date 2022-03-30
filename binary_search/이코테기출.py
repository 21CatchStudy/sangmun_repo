import sys
n = int(input())
array = list(map(int,sys.stdin.readline().rstrip().split()))

def solution(start, end, array):
    while(start<=end):
        mid = (start + end) // 2
        if mid==array[mid]:
            return mid
        elif mid>array[mid]:
            start = mid+1
        elif mid<array[mid]:
            end = mid-1
    return -1

print(solution(0,n-1,array)) #또는
print(solution(0,n,array))
#220323
from bisect import bisect_left

n = int(input())
nlist = list(map(int,input().split()))
answer = -1

for i in range(n):
    if nlist[i]==bisect_left(nlist,nlist[i]):
        answer = nlist[i]
        
if answer==-1:
    print(-1)
else:
    print(answer)   
