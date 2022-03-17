# 구현 - 시각:문제 조건


n = int(input())

# 0부터 N-99까지 시간선언

x = [00:00:00]
y = [23:59:59]
time_list = [00:00:00, 23:59:59]
result = 0

# 3을 잡아내는 코드
    for i in range(n) :
        result = x[i] += 1
        result = y[i] += 1

    while (x=y) :
        if i = 3 :
            result = i
            
    print(result)

    
    # H를 입력받기
h = int(input())

count = 0
for i in range(h + 1):
  for j in range(60):
    for k in range(60):
      # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
      if '3' in str(i) + str(j) + str(k):
        count += 1
print(count)
