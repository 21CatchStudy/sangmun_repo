https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    reserve_only = set(reserve) - set(lost)
    # 2,4,1,3,5 외에 겹치는 수가 없이 set으로 선언 
    lost_only = set(lost) - set(reserve)
    
    for reserve in reserve_only :
        #여분을 갖고있는 학생을 기준으로 코드를 나타냄
        front = reserve - 1
        # 3번이 2번에게 옷을 대여해줄 때
        back = reserve + 1
        if front in lost_only :
            #체육복이 필요하느냐? 에 대한 코드
            lost_only.remove(front)
        elif back in lost_only:
            lost_only.remove(back)
            
    return n - len(lost_only) # 5 - 0
    
print(solution(5,[2,4],[1,3,5]))
