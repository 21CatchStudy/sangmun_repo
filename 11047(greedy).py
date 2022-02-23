n, m = map(int, input().split())

coins = []
for _ in range (n) :
     coins.append (int(input()))
coins.sort(reverse = True)
    
    

answer = 0
for coin in coins : 
    if m >= coin : 
     answer += m // coin #몫 만큼 더하기
    m %= coin #나머지 할당
    if m <= 0 :
        break

print(answer)