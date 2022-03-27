from collections import deque

n, m, v  = map(int,input().split())


graph = [[] for _ in range(n + 1)]
# N(4) + 1
for _ in range(m):
  a, b = map(int, input().split())
  # 노드 연결 하기
  graph[a].append(b)
  graph[b].append(a)

#노드와 노드사이를 이어주기 위헤 필요한 코드값
# https://jinyes-tistory.tistory.com/223 이 부분을 참고하여 

visited = [False] * (n + 1)

#dfs 
def dfs(graph, v, visited) :
    visited[v] = True
    print(v, end= ' ') 
    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)


#bfs 
def bfs(graph, v, visited) :
    visited = [False] * (n + 1)
    queue = deque([v])
    visited[v] = True
    while queue :
        pop = queue.popleft()
        print(pop, end = ' ')
        for i in graph[pop] :
            if not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(graph, v, visited)
print()
bfs(graph, v, visited)
