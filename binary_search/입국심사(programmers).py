def solution(n, times):
    answer = 0
    left = 1
    right = max(times) * n
    
    while left < right :
        mid = (left + right) // 2
        total = 0
        
        for time in times :
            total += mid // time
            
            if total >= n :
                break
        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 많거나 같은 경우
        if total >= n :
            answer = mid
            right = mid - 1
            
        elif total < n :
            left = mid + 1
            
            
        
    return answer
