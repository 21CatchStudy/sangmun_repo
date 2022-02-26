#https://www.acmicpc.net/problem/1439

s = input()

timer_0 = 0 #이 두개의 변수들은 0과 1의 구분을 짓기위한 
timer_1 = 0 #변수초기화 형식이라고 생각하면 편하다.

if s[0] == '0' :
    timer_0 += 1
else :
    timer_1 += 1 


for i in range(len(s)+1) :
    
    if s[i] !=  s[i+1] :
        if s[i+1] == '0' :
            timer_0 += 1 
        else :
            timer_1 += 1

print(min(timer_0, timer_1))
