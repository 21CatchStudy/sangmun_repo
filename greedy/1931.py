# https://www.acmicpc.net/problem/1931

meetingroom = int(input())
setting = []
 

for i in range(meetingroom) :
    time_start, time_end = map(int, input().split()) # 처음 시작 끝 시작
    setting.append([time_start, time_end]) #시간의 시작과 끝을 튜플,리스트로 정렬
setting = sorted(setting, key=lambda a:a[0]) #start 값을 +1 (5,5)(4,5) 한가지만 하면 start는 1
setting = sorted(setting, key=lambda a:a[1]) #(5,5)(4,5) 둘다 선언해줘야 start 2

start = 0
end = 0

for i,j in setting : 
    if i >= end : # 시간이 올라가니 시작시간은 커야함 1-2, 2-3 : 
        start += 1
        end = j
        if i < 0 :
            break
print(start)
