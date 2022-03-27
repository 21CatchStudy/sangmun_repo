#dfs로 접근을 해야할 문제같아보였다
#상하좌우로 인접한 노드들의 방문을 거쳐 가는것이기 때문이였다
#정렬코드로 오름차순의 결과값을 나타내야하는 건 알았지만, len함수의 활용을 사용하지 못하였다
# https://www.acmicpc.net/problem/2667

n = int(input())
num = 0
#0 or 1 
graph = []
graph.append(list(map(int,input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x,y) :
    if x <= -1 or x >= n or y <= -1 or y >= m :
        return False
    if graph[x][y] == 0 :
        graph[x][y] = 1
        
        
        return True
    return False

result = 0
cnt = 0
cnt = sorted()
for i in range(n) :
    for j in range(m) :
        if dfs(i) == True :
            result == 1
for i in range(n, n+1):
    for j in range(m, m+1):
        for k in (n,m) :
            cnt += [i],[j],[k]

print(result)
print(i)
print(j)
print(k)





n = int(input())
graph = []
num = []

for i in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def DFS(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            DFS(nx, ny)
        return True
    return False


count = 0
result = 0

for i in range(n):
    for j in range(n):
        if DFS(i, j) == True:
            num.append(count)
            result += 1
            count = 0

num.sort()
print(result)
for i in range(len(num)):
    print(num[i])
