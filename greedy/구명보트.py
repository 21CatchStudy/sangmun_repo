# Point *
# 접근을 할때 k의 개수를 구하며 index의 자리값 1부터 , n+1이 필요하니까
# 각 수를 하나의 인덱스를 만들어서 =+1 
#index[0:10] index[i+1]

#https://programmers.co.kr/learn/courses/30/lessons/42885

*오류코드*

"""def solution(number, k) :
    a = sorted([19,12,14,92,94,24])
    for _ in range(k) :
         for i in range(0,len(number)-1) :
           number = number([index i] + number([index i+1])
         if number < k :
            print(max(number))
         if number > k :
            print(min(number))
        
    return number"""


*참고*
def solution(people, limit):
    answer = 0
    people.sort()
    merge_boat,alone_boat = 0, len(people) - 1
    
    while merge_boat <= alone_boat :
        answer += 1
        
        # 70, 80 이 더 크다 생각하고 +1
        
        if people[merge_boat]  + people[alone_boat] <= limit:
            merge_boat += 1
            alone_boat -= 1
        
        
    return  answer
