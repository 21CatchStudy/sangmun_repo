from collections import deque

c = int(input())
n = int(input())
#컴퓨터(노드) , 네트워크(간선) 쌍 수

a, b = map(int, input().split())
#쌍의 수

#POINT 쌍의 수가 서로 이어지려면 노드를 선언해주어야함
graph = [ []for _ in range   (c+1)]
graph[a].append(b)
graph[b].append(a)

#bfs , dfs 를 구별하여 선언해주는 것이 현 생각


def dfs(graph, c, visited) :
    visited[c] = True
    for i in graph[c] :
        if not visited[i] :
            dfs(graph, c, visited) 
        
                



def bfs(graph, c, visited) :
    queue = deque([c])
    visited[c] = True
    while queue :
        v = queue.popleft()
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True
    

cnt = 0

#1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.
for i in graph[1,2,3,5,6] :
    cnt += 1
    if graph[4,7] :
        continue

print(cnt) 
>>>>>>>>>>>>>>>>>>>>>>>>>>

# 모색 방안
# 1번의 방향으로만 이동하면 되기때문에 dfs를 선언하여 결과값이 나오게 한다.

n = int(input())
t = int(input())
graph = [[0] * n for i in range(n)]
visit = [0 for i in range(n)]
# 행이 n개인 2차원 리스트(인접리스트)
# visit n 부분에 한번씩 방문
# 간선의 쌍 부분을 선언 쌍 부분은 a,b
for i in range(t):
    a,b = map(int,input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

#dfs 바이러스가 1번에 올때.
def dfs(v):
    visit[v] = 1
    for i in range(n):
        if graph[v][i] == 1 and visit[i] == 0:
            dfs(i)

#Greedy 개념으로 방문할때 증가
#dfs를 돌지않은 숫자 나머지 카운트

dfs(0)
cnt = 0
for i in range(1, n):
    if visit[i] == 1:
        cnt += 1
print(cnt)
