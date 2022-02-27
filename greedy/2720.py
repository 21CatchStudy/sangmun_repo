# https://www.acmicpc.net/problem/2720

for _ in range(int(input())) : # 반복문안에 입력문 선언가능 이때는 3달러의 범위로 정하기로함
    k = int(input()) # 124의 숫자를 입력
    c = [25, 10, 5, 1] # 리암이 줘야할 거스름돈
    a = [] 
    for i in c :
     a.append(k//i)  # 25 //
     k = k%i
    

    print(*a)
