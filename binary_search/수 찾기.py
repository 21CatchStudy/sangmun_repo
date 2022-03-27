# https://www.acmicpc.net/problem/1920

def binary_search(target, array, start=0, end=None) :
    if end == None :
        end = len(array) - 1 
    if start > end :
        return 0 #start 인덱스가 end보다 커져버리면 나눠져 탐색했지만 target을 발견못했으므로 0을 리턴
    mid = (start + end) // 2

    if target == array[mid] :
        return 1 

    elif target < array [mid] :
        end = mid - 1 # end에서 mid가 작으면 위치할 때 까지 -1 씩 이동
    
    elif target > array [mid] :
        start = mid + 1  #이것보다 크게되면 mid 까지 +1 씩 증가
    
    return binary_search(target, array, start, end) 

n = int(input())
n_list = list(map(int,input().split()))
sorted_list = sorted(n_list)


m = int(input())
m_list = list(map(int,input().split()))

#m_list안에서 n을 확인하는 코드
for i in range(len(m_list())) : 
    print(binary_search(m_list[i], sorted_list)) 
