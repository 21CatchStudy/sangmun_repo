import sys
input = sys.stdin.readline

n = int(input())

array = []
for i in range(n):
    a, b = map(int, input(). split())
    array.append([a, b])
    
s_array = sorted(array) #sorted 형식의 정렬 

for i in range(n) :
    print(s_array[i][0], s_array[i][1]) # i가 0~4 범위로 돌아가며 인덱싱
