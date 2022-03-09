* #치킨배달
***

```*POINT*
#2차원 행렬로 생각해낸다
#abs 절대값으로 - 부호를 표현합니다
#시간초과에 유의해야합니다
#치킨집을 구한다, 집을 구한다
from itertools import combinations
import sys
n,m = map(int,input().split()) 
s,c,h = [], [], []
for i in range(n):
    a = list(map(int,input().split()))
    s.append(a)
    for j in range(n):
        if a[j] == 2: c.append([i,j])
        if a[j] == 1: h.append([i,j])
        #1번은 집, 2번은 치킨집 리스트 선언후 행렬로 포함
empty = 0
house = 1
chicken = 2
#도시의 칸은 r,c 1부터 시작한다 1,1
#도시의 치킨거리는 모든 집의 치킨거리의 합이다
#치킨집의 개수는 M보다 크거나 같고 13보다 작거나 같다
while True :
    if chicken >= m or chicken <= 13 :
c = combinations(c,m)
#폐업시키자않을 치킨집 최대 M, 도시의 치킨거리의 최소값
result = 10000000000
for k in c :
    min_result = 100000000000
#치킨집의 가장 작은 치킨거리를 출력해주는 선언문
    for i,j in h :
        min_num = 0
        for x,y in k :
            min_num = min(min_num, abs(x - i) + abs(y -j))
            #4-5가 되면 -1로 인해 abs 선언
        min_result += min_num
    result = min(result, min_result)
print(result) 
```


* # 뱀
*먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다. 뱀의 세부사항을 캐치하지못함
*만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다
*만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
***
정답코드
```
import sys    
from collections import deque
input = sys.stdin.readline
def changedir(cha):
    if cha == "L":
        if direction == [1, 0]:
            return [0, 1]
        elif direction == [-1, 0]:
            return [0, -1]
        elif direction == [0, 1]:
            return [-1, 0]
        elif direction == [0, -1]:
            return [1, 0]
    elif cha == "D":
        if direction == [1, 0]:
            return [0, -1]
        elif direction == [-1, 0]:
            return [0, 1]
        elif direction == [0, 1]:
            return [1, 0]
        elif direction == [0, -1]:
            return [-1, 0]
    
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
     # 루트 L과 D의 선언을 통해   

def check(x,y) :
    if[x,y] in q :
        return False
    return True
n = int(input())
direction = 1
time = 1 

while True:
        y, x = y + dy[direction], x + dx[direction]
        return time


L = int(input())
    times = {}
    for i in range(L):
        X, C = input().split()
        ```
        
**오답코드**
첫째 줄 보드의 크기
k 사과위치 l 이동경로
 행과 열의 범위 dx,dy로 선언을 하였다
  문자열 이기때문에 타입변수를 주고 왼쪽 오른쪽으로 선언하였다
```
n = int(input())
 
k,l = list(map(int,input().split))
 
dx = [1,0,-1,0]
dy = [-1,1,0,-1]
 
k = dx + dy
move_types = ['L', 'D']
 
x = int(0)
 
cnt = 0
start = 0

for go in (l) :
    while start > x : 
        게임이 계속 시작될 때
     for i in(len(move_types)) :
        for j in(int(x)) :
            if x == 0 :
                cnt += k
                cnt = move_types + 1

print(cnt)
```
