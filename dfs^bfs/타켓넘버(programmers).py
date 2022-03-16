def solution(numbers, target):
    n = len(numbers)
    answer = 0
    def dfs(index, result):
        if index == n:
            if result == target:
                nonlocal answer
                #변수 무제한이 선언될 수 있으니 nonlocal 제어
                answer += 1
            return
        else:
            dfs(index+1, result+numbers[index])
            dfs(index+1, result-numbers[index])
    dfs(0,0)
    return answer
