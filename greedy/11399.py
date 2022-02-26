n = int(input())

data = list(map(int, input(). split()))
data.sort()

result = 0

for i in range(n): #전체 사람의 수
    for j in range(i  + 1): #돈을 인출하는 사람들의 최소값
        result += data[j]
    

    


print(result)
