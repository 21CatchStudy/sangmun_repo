#처음 다익스트라 알고리즘 접근법 - 한 지점에서 다른 모든 지점까지의 계산때문
import sys
input = sys.stdin.readline
INF = int(1e9)


n,m = map(int,input().split())
graph = [[INF] * ( n + 1 ) for _ in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)



for _ in range(m) :
    a,b = map(int, input().split())
    graph[a].append((b))

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i] :
            min_value = distance[i]
            index = i
    return index



def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    
    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        
        for j in graph[now] :
            cost = distance[now] + j[1]

            if cost < distance[j[0]] :
                distance[j[0]] = cost

    dijkstra(start)

for i in range(1, n+1) :
    if distance[i] == INF :
        print("1")
    else:
        print(distance[i])






#플로이드 워셜 알고리즘

INF = int(1e9)


n,m = map(int,input().split())
graph = [[INF] * ( n + 1 ) for _ in range(n + 1)]

for a in range (1, n+1) : 
    for b in range (1, n+1) :
        if a == b :
            graph[a][b] = 0

for _ in range(m) :
    a, b = map(int,input().split())
    graph[a][b] = 1

for k in range(1, n+1) :
    for a in range(1, n+1) :
        for b in range(1, n+1) :
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0 

for i in range(1, n+1) :
    count = 0
    for j in range(1, n+1) :
        if graph[i][j] != INF or graph[j][i] != INF :
            count += 1
    if count == n :
        result += 1
print(result)

 
