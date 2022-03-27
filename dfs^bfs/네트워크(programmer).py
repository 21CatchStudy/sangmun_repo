def solution(n, computers):            
    
    def DFS(i):
        visited[i] = 1
        for a in range(n):
            if computers[i][a] and not visited[a]:
                DFS(a)      
                #DFS로 방문해준다.
                
    answer = 0
    visited = [0 for i in range(len(computers))]
    for i in range(n):
        if not visited[i]:
            DFS(i)
            answer += 1
            #방문 처리하지 않은 마지막 까지 카운트.
        
    return answer
