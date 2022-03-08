#https://www.acmicpc.net/problem/3190

n = int(input())
# 첫째 줄 보드의 크기
k,l = list(map(int,input().split))
# k 사과위치 l 이동경로
dx = [1,0,-1,0]
dy = [-1,1,0,-1]
# 행과 열의 범위 dx,dy로 선언을 하였다
k = dx + dy
move_types = ['L', 'D']
# 문자열 이기때문에 타입변수를 주고 왼쪽 오른쪽으로 선언하였다
x = int(0)
# 정수 x를 int로 선언
cnt = 0
start = 0

for go in (l) :
    while start > x : 
        #게임이 계속 시작될 때
     for i in(len(move_types)) :
        for j in(int(x)) :
            if x == 0 :
                cnt += k
                cnt = move_types + 1

print(cnt)
